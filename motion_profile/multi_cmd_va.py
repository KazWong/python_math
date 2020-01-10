import matplotlib.pyplot as plt
import numpy as np
import math

r = 10
dt = 0.1
Vt =   np.array([0.00000])
Vn =   np.array([0.60000, 1.00000, 1.50000, 3.60000, 1.00000, -1.0000, -2.3400, 2.35000, 1.42000, 0.0000])
At =   np.array([0.00000])
An =   np.array([0.00011, 0.00011, 0.00001, 0.00001, 0.00001, 0.00001, 0.00001, 0.00001, 0.00001, 0.00001])
Amax = np.array([2.00000, 1.20000, 2.60000, 2.30000, 3.60000, 5.77000, 2.00000, 2.00000, 2.00000, 2.00000])
St =   np.array([0.00000])
Jt =   np.array([])
t = np.array([])
total_T = 0.0
total_n = 0

def Profile(Vn, Amax, i):
  T = 0.0
  global total_T, St, Vt, At, Jt, total_n
  ### solve T using maximum accel ###
  if (At[-1] == 0.0 and An[i] == 0.0):
	  T = abs(3*(Vn - Vt[-1])/(2*Amax))
  else:
    if (At[-1] <= Amax):
      rt = math.sqrt(Amax**2 + An[i]*At[-1] - Amax*(An[i] + At[-1]))
    else:
      Amax = At[-1]
      rt = 0
    T11 = 3*(Vn - Vt[-1])*( rt + (At[-1] + An[i] + Amax) ) / ((At[-1] + An[i] + Amax)**2 + Amax*(An[i] + At[-1]) - At[-1]*An[i] - Amax**2)
    T22 = 3*(Vn - Vt[-1])*( -rt + (At[-1] + An[i] + Amax) ) / ((At[-1] + An[i] + Amax)**2 + Amax*(An[i] + At[-1]) - At[-1]*An[i] - Amax**2)
    T = min([abs(T11), abs(T22)])

  T2 = T*T
  T3 = T2*T

  ### solve coefficient ###
  A = np.array([[1, 0,   0,    0], 
                [0, 1,   0,    0], 
                [1, T,  T2,   T3], 
                [0, 1, 2*T, 3*T2]])
  B = np.array([Vt[-1], At[-1], Vn, An[i]])
  a = np.linalg.inv(A).dot(B)

  ### Plot ###
  t1 = np.linspace(0, dt, dt*1000)
  t2 = t1*t1
  t3 = t2*t1

  pos  = St[-1] + a[0]*t1 + a[1]*t2/2 + a[2]*t2/3 + a[3]*t3/4
  vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3
  acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2
  jerk = 2*a[2] + 6*a[3]*t1
  
  St = np.append(St, pos)
  Vt = np.append(Vt, vel)
  At = np.append(At, acc)
  Jt = np.append(Jt, jerk)
  total_T = T + total_T
  total_n = len(t1) + total_n

for i in range(r):
  Profile(Vn[i], Amax[i], i)

t1 = np.linspace(0, r*dt, total_n)
St = np.delete(St, 0)
Vt = np.delete(Vt, 0)
At = np.delete(At, 0)

plt.suptitle('v maxa')
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(t1, St)
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(t1, Vt)
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(t1, At)
plt.subplot(414)
plt.ylabel('jerk')
plt.plot(t1, Jt)
plt.show()

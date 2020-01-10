import matplotlib.pyplot as plt
import numpy as np
import math

r = 30
dt = 0.1
Vt =   np.array([0.00000])
At =   np.array([0.00000])
St =   np.array([0.00000])
Jt =   np.array([0.00000])
t = np.array([])
total_T = 0.0
total_n = 0

'''
Vn =   np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
An =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Jn =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
#Amax = np.array([4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 
#                 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000])
Amax = np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
#
'''

### Vn = 2 -> 0 -> -2 ###
Vn =   np.array([1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000])
An =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Jn =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Amax = np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000])
'''
Amax = np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
'''
#

'''
### Vn = 2 ###
Vn =   np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000])
An =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Jn =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Amax = np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000])
#
'''


'''
### Vn = -2 ###
Vn =   np.array([-2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
An =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Jn =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Amax = np.array([-2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
#
'''


def Profile(Vn, Amax, i):
  global total_T, St, Vt, At, Jt, An, Jn, total_n, dt
  t = dt
  T = 0.0
  ### solve T using maximum accel ###
  if (Vn < Vt[-1]):
    Amax = -1*Amax
  if ( (At[-1] > -1e-8 and At[-1] < 1e-8) and (An[i] > -1e-8 and An[i] < 1e-8) ):
	  T = 3*(Vn - Vt[-1])/(2*Amax)
  else:
    if (abs(At[-1]) > abs(Amax)):
  	  rt = 0
  	  Amax = At[-1]
  	  print('why', Amax)
    else:
      rt = math.sqrt(Amax**2 + An[i]*At[-1] - Amax*(An[i] + At[-1]))
    T11 = 3*(Vn - Vt[-1])*( rt + (At[-1] + An[i] + Amax) ) / ((At[-1] + An[i] + Amax)**2 + Amax*(An[i] + At[-1]) - At[-1]*An[i] - Amax**2)
    T22 = 3*(Vn - Vt[-1])*( -rt + (At[-1] + An[i] + Amax) ) / ((At[-1] + An[i] + Amax)**2 + Amax*(An[i] + At[-1]) - At[-1]*An[i] - Amax**2)
    T = min([abs(T11), abs(T22)])
  
  if (T > 1e-8 or T < -1e-8):
    T2 = T*T
    T3 = T2*T
    T4 = T3*T
    T5 = T4*T

    A = np.array([[1, 0,   0,    0,     0,     0], 
                  [0, 1,   0,    0,     0,     0], 
                  [0, 0,   1,    0,     0,     0], 
                  [1, T,  T2,   T3,    T4,    T5], 
                  [0, 1, 2*T, 3*T2,  4*T3,  5*T4], 
                  [0, 0,   2,  6*T, 12*T2, 20*T3]])
    B = np.array([Vt[-1], At[-1], Jt[-1], Vn, An[i], Jn[i]])
    a = np.linalg.inv(A).dot(B)

    ### Plot ###
    if (t > abs(T)):
  	  t = T
  else:
    a = np.array([Vt[-1], 0, 0, 0, 0, 0])
  
  t1 = np.linspace(0, abs(t), abs(t)*1000)
  t2 = t1*t1
  t3 = t2*t1
  t4 = t3*t1
  t5 = t4*t1

  pos  = St[-1] + a[0]*t1 + a[1]*t2/2 + a[2]*t2/3 + a[3]*t3/4 + a[4]*t4/5 + a[5]*t5/6
  vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3 + a[4]*t4 + a[5]*t5
  acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2 + 4*a[4]*t3 + 5*a[5]*t4
  jerk  = 2*a[2] + 6*a[3]*t1 + 12*a[4]*t2 + 20*a[5]*t3
  
  
  pos = np.delete(pos, 0)
  vel = np.delete(vel, 0)
  acc = np.delete(acc, 0)
  jerk = np.delete(jerk, 0)

  St = np.append(St, pos)
  Vt = np.append(Vt, vel)
  At = np.append(At, acc)
  Jt = np.append(Jt, jerk)
  total_T = t + total_T
  total_n = len(pos) + total_n


for i in range(r):
  Profile(Vn[i], Amax[i], i)

t1 = np.linspace(0, total_T, total_n)
St = np.delete(St, 0)
Vt = np.delete(Vt, 0)
At = np.delete(At, 0)
Jt = np.delete(Jt, 0)

plt.suptitle('v maxa j')
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

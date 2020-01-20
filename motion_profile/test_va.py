from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math

r = 60
dt = 0.05
Vt =   np.array([0.00000])
At =   np.array([0.00000])
St =   np.array([0.00000])
Jt =   np.array([])
t = np.array([])
total_T = 0.0
total_n = 0
t = 0.0
T = 0.0

'''
Vn =   np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
An =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
#Amax = np.array([4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 
#                 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000, 4.00000])
Amax = np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
'''


### Vn = 2 -> 0 -> -2 ###
Vn =   np.array([1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000, -1.0000])
An =   np.array([0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000,
                 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000])
Amax = np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000,
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000])
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

Amax = np.array([2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 
                 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000, 2.00000])

Amax = np.array([-2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, 
                 -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000, -2.0000])
'''
#


def Profile(Vn, Amax, i):
  global total_T, St, Vt, At, Jt, total_n, dt, t, T
  
  ### solve T using maximum accel ###
  '''
  if (Vt[-1] > Vn):
	  Amax = -1*Amax
  if (At[-1] == 0.0):#( (At[-1] > -1e-8 and At[-1] < 1e-8) and (An[i] > -1e-8 and An[i] < 1e-8) ):
	  T = 3*(Vn - Vt[-1])/(2*Amax)
	  print('At = 0.0', T)
  else:
    print('V', Vn, Vt[-1], 'A', Amax, At[-1])
    rt = math.sqrt(Amax**2 + An[i]*At[-1] - Amax*(An[i] + At[-1]))
    T11 = 3*(Vn - Vt[-1])*( rt + (At[-1] + An[i] + Amax) ) / ((At[-1] + An[i] + Amax)**2 + Amax*(An[i] + At[-1]) - At[-1]*An[i] - Amax**2)
    T22 = 3*(Vn - Vt[-1])*( -rt + (At[-1] + An[i] + Amax) ) / ((At[-1] + An[i] + Amax)**2 + Amax*(An[i] + At[-1]) - At[-1]*An[i] - Amax**2)

    Tl = []
    if (T11 > 0):
      Tl.append(T11)
    if (T22 > 0):
      Tl.append(T22)
      T = min(Tl)
      t = 0.0
    print('T', T, T11, T22)
  '''
  
  T = 0.75
  t = 0.0
  
  if (T > 1e-8 or T < -1e-8):
    T2 = T*T
    T3 = T2*T

    
    ### solve coefficient ###
    A = np.array([[1, 0,   0,    0], 
                  [0, 1,   0,    0], 
                  [1, T,  T2,   T3], 
                  [0, 1, 2*T, 3*T2]])
    B = np.array([Vt[-1], At[-1], Vn, An[i]])
    a = np.linalg.inv(A).dot(B)
    
    '''
    m = np.array( [1., T, T*T, T*T*T, 0., 1., 2.*T, 3.*T*T])
    det =  1./(m[3]*T)
    a = np.array([
								Vt[-1], 
								At[-1],
								det*( Vt[-1]*( -m[7] ) + At[-1]*( -m[1] * m[7] + m[3] ) + Vn*( m[7] ) + An[i]*( -m[3] ) ),
								det*( Vt[-1]*( m[6] ) + At[-1]*( m[1] * m[6] - m[2] ) + Vn*( -m[6] ) + An[i]*( m[2] ) )] )
		'''
  dt2 = dt
  if (dt2 > T):
	  dt2 = T	
  print('t', total_T, t, dt2)
  print()
  
  ### Plot ###
  t1 = np.linspace(t, abs(dt + t), abs(dt2 + t)*1000)
  t2 = t1*t1
  t3 = t2*t1
  t = dt2 + t

  pos  = St[-1] + a[0]*t1 + a[1]*t2/2 + a[2]*t2/3 + a[3]*t3/4
  vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3
  acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2
  jerk = 2*a[2] + 6*a[3]*t1
  
  pos = np.delete(pos, 0)
  vel = np.delete(vel, 0)
  acc = np.delete(acc, 0)
  jerk = np.delete(jerk, 0)
    
  St = np.append(St, pos)
  Vt = np.append(Vt, vel)
  At = np.append(At, acc)
  Jt = np.append(Jt, jerk)
  total_T = dt2 + total_T
  total_n = len(pos) + total_n


for i in range(r):
  Profile(Vn[i], Amax[i], i)

t1 = np.linspace(0, total_T, total_n)
St = np.delete(St, 0)
Vt = np.delete(Vt, 0)
At = np.delete(At, 0)

plt.suptitle('v maxa')

plt.subplot(211)
line_S, = plt.plot(t1, St, label='S')
plt.subplot(211)
line_V, = plt.plot(t1, Vt, label='V')
plt.subplot(211)
line_A, = plt.plot(t1, At, label='A')
plt.subplot(211)
plt.xlabel('t')
plt.ylabel('m, m/s, m/s2, m/s3')
line_J, = plt.plot(t1, Jt, label='J')
plt.legend(handles=[line_S, line_V, line_A, line_J])
plt.title("SVAJ") 

 
yy = abs(fft(Vt)/total_n)
yy_half = yy[range(int(total_n/40))]
xx = np.arange(len(Vt))
xx_halft = xx[range(int(total_n/40))]
plt.subplot(212) 
line_fftV, = plt.plot(xx_halft, yy_half, label='V') 

yy = abs(fft(At)/total_n)
yy_half = yy[range(int(total_n/40))]
xx = np.arange(len(At))
xx_halft = xx[range(int(total_n/40))]
plt.subplot(212) 
line_fftA, = plt.plot(xx_halft, yy_half, label='A') 
plt.xlabel('Freq')
plt.title("FFT Square")
plt.legend(handles=[line_fftV, line_fftA])

#plt.legend(handles=[line_up, line_down])
plt.show()

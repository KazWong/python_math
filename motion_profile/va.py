import matplotlib.pyplot as plt
import numpy as np
import math

V0 = 0.0
Vn = 1.0
A0 = 1.7227
An = 0.0000
Amax = 2.0
T = 0.0



### solve T using maximum accel ###
if (Amax != 0.0 and T == 0.0):
	T11 = 0.0
	T12 = 0.0
	
	'''
	T11 = 3*((-V0 + Vn)*math.sqrt(9*A0**2 - A0*Amax + A0*An - 9*A0 + Amax**2 - Amax*An) - (V0 - Vn)*(A0 + Amax + An))/(-8*A0**2 + 3*A0*Amax + A0*An + 9*A0 + 3*Amax*An + An**2)
	T22 = 3*(V0 - Vn)*(-A0 - Amax - An + math.sqrt(9*A0**2 - A0*Amax + A0*An - 9*A0 + Amax**2 - Amax*An))/(-8*A0**2 + 3*A0*Amax + A0*An + 9*A0 + 3*Amax*An + An**2)
  '''

	if (V0 > Vn):
		Amax = -1*Amax
	if (A0 == 0.0 and An == 0.0):
		T = abs(3*(Vn - V0)/(2*Amax))
	else:
		T11 = 3*(Vn - V0)*( math.sqrt(Amax**2 + An*A0 - Amax*(An + A0)) + (A0 + An + Amax) ) / ((A0 + An + Amax)**2 + Amax*(An + A0) - A0*An - Amax**2)
		T22 = 3*(Vn - V0)*( -math.sqrt(Amax**2 + An*A0 - Amax*(An + A0)) + (A0 + An + Amax) ) / ((A0 + An + Amax)**2 + Amax*(An + A0) - A0*An - Amax**2)
		#T = min([abs(T11), abs(T22)])#min([n for n in [T11, T22]  if n>0])
		print('T11 = ', T11)
		print('T22 = ', T22)
		Tl = []
		if (T11 > 0):
			Tl.append(T11)
		if (T22 > 0):
			Tl.append(T22)
		T = min(Tl)
	print('T = ', T)
	

T2 = T*T
T3 = T2*T



### solve coefficient ###
A = np.array([[1, 0,   0,    0], 
              [0, 1,   0,    0], 
              [1, T,  T2,   T3], 
              [0, 1, 2*T, 3*T2]])
B = np.array([V0, A0, Vn, An])
#B = B.reshape([-1, 1])
a = np.linalg.inv(A).dot(B)

'''
m = np.array( [1., T, T*T, T*T*T, 0., 1., 2.*T, 3.*T*T])
det =  1./(m[3]*T)
a = np.array([
     V0, 
     A0,
     det*( V0*( -m[7] ) + A0*( -m[1] * m[7] + m[3] ) + Vn*( m[7] ) + An*( -m[3] ) ),
     det*( V0*( m[6] ) + A0*( m[1] * m[6] - m[2] ) + Vn*( -m[6] ) + An*( m[2] ) )] )
print(c)
'''



### Plot ###
t1 = np.linspace(0, abs(T), abs(T*1000))
t2 = t1*t1
t3 = t2*t1

pos  = 0 + a[0]*t1 + a[1]*t2/2 + a[2]*t2/3 + a[3]*t3/4
vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3
acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2
jerk = 2*a[2] + 6*a[3]*t1

for i in range(4):
  print('a[', i ,'] = ', a[i])

plt.suptitle('v maxa')
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(t1, pos)
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(t1, vel)
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(t1, acc)
plt.subplot(414)
plt.ylabel('jerk')
plt.plot(t1, jerk)
plt.show()

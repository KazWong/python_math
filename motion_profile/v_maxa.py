import matplotlib.pyplot as plt
import numpy as np
import math

V0 = 0.0
Vn = 0.5
A0 = 1.0
An = 0.0001
MaxA = 1.124975

T11 = 3*((-V0 + Vn)*math.sqrt(9*A0**2 - A0*MaxA + A0*An - 9*A0 + MaxA**2 - MaxA*An) - (V0 - Vn)*(A0 + MaxA + An))/(-8*A0**2 + 3*A0*MaxA + A0*An + 9*A0 + 3*MaxA*An + An**2)
T22 = 3*(V0 - Vn)*(-A0 - MaxA - An + math.sqrt(9*A0**2 - A0*MaxA + A0*An - 9*A0 + MaxA**2 - MaxA*An))/(-8*A0**2 + 3*A0*MaxA + A0*An + 9*A0 + 3*MaxA*An + An**2)

print('T11 = ', T11)
print('T22 = ', T22)

T = T22#min([n for n in [T11, T22]  if n>0])

T2 = T*T
T3 = T2*T

A = np.array([[1, 0,   0,    0], 
              [0, 1,   0,    0], 
              [1, T,  T2,   T3], 
              [0, 1, 2*T, 3*T2]])
B = np.array([V0, A0, Vn, An])
#B = B.reshape([-1, 1])
a = np.linalg.inv(A).dot(B)


'''
m = np.array( [1, T, T*T, T*T*T, 0, 1, 2*T, 3*T*T])
det =  1./(m[2] * m[7] - m[3] * m[6])
c = [V0, 
     A0,
     det*( V0*( -m[0] * m[7] + m[4] * m[3] ) + A0*( -m[1] * m[7] + m[3] * m[5] ) + Vn*( m[7] ) + An*( -m[3] ) ),
     det*( V0*( m[0] * m[6] - m[4] * m[2] ) + A0*( m[1] * m[6] - m[2] * m[5] ) + Vn*( -m[6] ) + An*( m[2] ) )]
print(c)
'''


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

import matplotlib.pyplot as plt
import numpy as np
import math

#This algo assume A0, An is 0
A0 = 0.0
An = 0.0

#variable
V0 = 0.
Vn = 1.5
MaxA = 1.5

T = 3*(Vn - V0)/(2*MaxA)
print('T = ', T)

T2 = T*T
T3 = T2*T

A = np.array([[1, 0,   0,    0], 
              [0, 1,   0,    0], 
              [1, T,  T2,   T3], 
              [0, 1, 2*T, 3*T2]])
              
B = np.array([V0, A0, Vn, An])
B.reshape([-1, 1])

a = np.linalg.inv(A).dot(B)


t1 = np.linspace(0, T, T*10)
t2 = t1*t1
t3 = t2*t1

pos  = 0 + a[0]*t1 + a[1]*t2/2 + a[2]*t2/3 + a[3]*t3/4
vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3
acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2
jerk = 2*a[2] + 6*a[3]*t1

for i in range(4):
  print('a[', i ,'] = ', a[i])

plt.suptitle('v maxa, assume A0, An is 0.0')
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

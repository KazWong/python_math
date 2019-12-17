import matplotlib.pyplot as plt
import numpy as np
import math

T = 2.
V0 = 0.
Vn = 1.5
A0 = 0.
An = 0.0001
MaxA = 1.124975


v0 = V0
vn = Vn
a0 = A0
an = An
amax = MaxA

T11 = 3*((-v0 + vn)*math.sqrt(9*a0**2 - a0*amax + a0*an - 9*a0 + amax**2 - amax*an) - (v0 - vn)*(a0 + amax + an))/(-8*a0**2 + 3*a0*amax + a0*an + 9*a0 + 3*amax*an + an**2)
T22 = 3*(v0 - vn)*(-a0 - amax - an + math.sqrt(9*a0**2 - a0*amax + a0*an - 9*a0 + amax**2 - amax*an))/(-8*a0**2 + 3*a0*amax + a0*an + 9*a0 + 3*amax*an + an**2)
T = min([n for n in [T11, T22]  if n>0])

#T=3

print('T11 = ', T11)
print('T22 = ', T22)

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

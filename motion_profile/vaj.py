import matplotlib.pyplot as plt
import numpy as np

T = 10.
V0 = 0.
Vn = 1.
A0 = 0.
An = 0.
J0 = 0.
Jn = 0.


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
              
B = np.array([V0, A0, J0, Vn, An, Jn])
B.reshape([-1, 1])

a = np.linalg.inv(A).dot(B)


t1 = np.linspace(0, T, T*1000)
t2 = t1*t1
t3 = t2*t1
t4 = t3*t1
t5 = t4*t1

pos  = 0 + a[0]*t1 + a[1]*t2/2 + a[2]*t2/3 + a[3]*t3/4 + a[4]*t4/5 + a[5]*t5/6
vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3 + a[4]*t4 + a[5]*t5
acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2 + 4*a[4]*t3 + 5*a[5]*t4
jerk  = 2*a[2] + 6*a[3]*t1 + 12*a[4]*t2 + 20*a[5]*t3

for i in range(6):
  print(a[i])

plt.suptitle('vaj')
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
  


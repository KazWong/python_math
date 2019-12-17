import matplotlib.pyplot as plt
import numpy as np

T = 10.
X0 = 0.
Xn = 0.5
V0 = 0.
Vn = 1.


T2 = T*T
T3 = T2*T

A = np.array([[1, 0,   0,    0], 
              [0, 1,   0,    0],  
              [1, T,  T2,   T3], 
              [0, 1, 2*T, 3*T2]])
              
B = np.array([X0, V0, Xn, Vn])
B.reshape([-1, 1])

a = np.linalg.inv(A).dot(B)


t1 = np.linspace(0, T, T*10)
t2 = t1*t1
t3 = t2*t1

pos  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3
vel  = a[1] + 2*a[2]*t1 + 3*a[3]*t2
acc  = 2*a[2] + 6*a[3]*t1
jerk = [6*a[3]] * len(t1)

for i in range(4):
  print(a[i])

plt.suptitle('xv')
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
  


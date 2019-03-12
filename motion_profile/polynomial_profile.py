import matplotlib.pyplot as plt
import numpy as np

T = 2000.
X_s = 0.
X_e = 100.
V_s = 0.
V_e = 0.
A_s = 0.
A_e = 0.


T2 = T*T
T3 = T2*T
T4 = T3*T
T5 = T4*T

A = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [1, T, T2, T3, T4, T5], [0, 1, 2*T, 3*T2, 4*T3, 5*T4], [0, 0, 2, 6*T, 12*T2, 20*T3]])
B = np.array([X_s, V_s, A_s, X_e, V_e, A_e])
B.reshape([-1, 1])

a = np.linalg.inv(A).dot(B)


t = np.linspace(0, T, T*10)

pos = a[0] + a[1]*t + a[2]*t*t + a[3]*t*t*t + a[4]*t*t*t*t + a[5]*t*t*t*t*t
vel = a[1] + 2*a[2]*t + 3*a[3]*t*t + 4*a[4]*t*t*t + 5*a[5]*t*t*t*t
acc = 2*a[2] + 6*a[3]*t + 12*a[4]*t*t + 20*a[5]*t*t*t

for i in xrange(6):
  print a[i]

plt.subplot(311)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(t, pos)
plt.subplot(312)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(t, vel)
plt.subplot(313)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(t, acc)
plt.show()
  


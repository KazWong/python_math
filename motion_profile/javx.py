import matplotlib.pyplot as plt
import numpy as np

T = 2000.
X0 = 0.
Xn = 100.
V0 = 0.
Vn = 0.
A0 = 0.
An = 0.
J0 = 0.
Jn = 0.


T2 = T*T
T3 = T2*T
T4 = T3*T
T5 = T4*T
T6 = T5*T
T7 = T6*T

A = np.array([[1., 0.,   0.,    0.,     0.,     0.,      0.,      0.], 
              [0., 1.,   0.,    0.,     0.,     0.,      0.,      0.], 
              [0., 0.,   1.,    0.,     0.,     0.,      0.,      0.], 
              [0., 0.,   0.,    1.,     0.,     0.,      0.,      0.],
              [1.,  T,   T2,    T3,     T4,     T5,      T6,      T7], 
              [0., 1., 2.*T, 3.*T2,  4.*T3,  5.*T4,   6.*T5,   7.*T6], 
              [0., 0.,   2.,  6.*T, 12.*T2, 20.*T3,  30.*T4,  42.*T5],
              [0., 0.,   0.,    6.,  24.*T, 60.*T2, 120.*T3, 210.*T4]])
              
B = np.array([X0, V0, A0, J0, Xn, Vn, An, Jn])
B.reshape([-1, 1])

a = np.linalg.inv(A).dot(B)


t1 = np.linspace(0, T, T*10)
t2 = t1*t1
t3 = t2*t1
t4 = t3*t1
t5 = t4*t1
t6 = t5*t1
t7 = t6*t1

pos  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3 + a[4]*t4 + a[5]*t5 + a[6]*t6 + a[7]*t7
vel  = a[1] + 2*a[2]*t1 + 3*a[3]*t2 + 4*a[4]*t3 + 5*a[5]*t4 + 6*a[6]*t5 + 7*a[7]*t6
acc  = 2*a[2] + 6*a[3]*t1 + 12*a[4]*t2 + 20*a[5]*t3 + 30*a[6]*t4 + 42*a[7]*t5
jerk = 6*a[3] + 24*a[4]*t1 + 60*a[5]*t2 + 120*a[6]*t3 + 210*a[7]*t4

for i in range(8):
  print(a[i])

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
  


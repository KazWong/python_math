import numpy as np
import matplotlib.pyplot as plt
from ..motion_profile.linear import VAJ, XVAJ
from ..simtools import *


sampling_rate = 1000.
clock = Time(1./sampling_rate)


### VAJ
print('********************************************************************')
print('')
print('VAJ:')
x0 = [0., 0., 0.]
xn = [5., 0., 0.]
T = 10.
shift = 5.0
end_time = 20.

x = VAJ(T, x0, xn)

clock.Reset()
clock.Offline(shift)
while (clock.now() < end_time):
    clock.Tick()
    x.Update()

y = x.Y()
y = y.reshape([-1, 3])
y0 = x.Pos()
print(y[:,0])

V0 = x0[0];Vn = xn[0];A0 = x0[1];An = xn[1];J0 = x0[2];Jn = xn[2]

T2 = T*T;T3 = T2*T;T4 = T3*T;T5 = T4*T

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
t2 = t1*t1;t3 = t2*t1;t4 = t3*t1;t5 = t4*t1;t6 = t5*t1

pos = 0 + a[0]*t1 + a[1]*t2/2. + a[2]*t3/3. + a[3]*t4/4. + a[4]*t5/5. + a[5]*t6/6.
vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3 + a[4]*t4 + a[5]*t5
acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2 + 4*a[4]*t3 + 5*a[5]*t4
jerk  = 2*a[2] + 6*a[3]*t1 + 12*a[4]*t2 + 20*a[5]*t3

print(vel)

sa = x.a()
print("Sumulation\t", sa)
print("Ground true\t", a)
print()

plt.figure()
plt.suptitle('vaj')
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(t1, pos, label='ground true')
plt.plot(x.timespace(), y0, label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(t1, vel, label='ground true')
plt.plot(x.timespace(), y[:,0], label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(t1, acc, label='ground true')
plt.plot(x.timespace(), y[:,1], label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)
plt.subplot(414)
plt.ylabel('jerk')
plt.plot(t1, jerk, label='ground true')
plt.plot(x.timespace(), y[:,2], label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)


### XVAJ
print('********************************************************************')
print('')
print('XVAJ:')
x0 = [0., 0., 0., 0.]
xn = [10., 5., 0., 0.]
T = 10.
shift = 5.0
end_time = 20.

x = XVAJ(T, x0, xn)

clock.Reset()
clock.Offline(shift)
while (clock.now() < end_time):
    clock.Tick()
    x.Update()

y = x.Y()
y = y.reshape([-1, 4])
print(y[:,0])

X0 = x0[0];Xn = xn[0];V0 = x0[1];Vn = xn[1];A0 = x0[2];An = xn[2];J0 = x0[3];Jn = xn[3]

T2 = T*T;T3 = T2*T;T4 = T3*T;T5 = T4*T;T6 = T5*T;T7 = T6*T

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


t1 = np.linspace(0, T, T*1000)
t2 = t1*t1;t3 = t2*t1;t4 = t3*t1;t5 = t4*t1;t6 = t5*t1;t7 = t6*t1

pos  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3 + a[4]*t4 + a[5]*t5 + a[6]*t6 + a[7]*t7
vel  = a[1] + 2*a[2]*t1 + 3*a[3]*t2 + 4*a[4]*t3 + 5*a[5]*t4 + 6*a[6]*t5 + 7*a[7]*t6
acc  = 2*a[2] + 6*a[3]*t1 + 12*a[4]*t2 + 20*a[5]*t3 + 30*a[6]*t4 + 42*a[7]*t5
jerk = 6*a[3] + 24*a[4]*t1 + 60*a[5]*t2 + 120*a[6]*t3 + 210*a[7]*t4

print(pos)

sa = x.a()
print("Sumulation\t", sa)
print("Ground true\t", a)
print()


plt.figure()
plt.suptitle('xvaj')
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(t1, pos, label='ground true')
plt.plot(x.timespace(), y[:,0], label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(t1, vel, label='ground true')
plt.plot(x.timespace(), y[:,1], label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(t1, acc, label='ground true')
plt.plot(x.timespace(), y[:,2], label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)
plt.subplot(414)
plt.ylabel('jerk')
plt.plot(t1, jerk, label='ground true')
plt.plot(x.timespace(), y[:,3], label='vaj, t shift: ' + str(shift))
plt.legend(framealpha=1, frameon=True)


plt.show()

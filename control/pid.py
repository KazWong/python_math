import matplotlib.pyplot as plt
import numpy as np
import math

V0 = 0.944856
Vn = 1.0
A0 = 1.7227
An = 0.0000
Amax = 2.0
T = 0.0



### PID ###
u[i][1] = u[i][0];

e[i][2] = e[i][1];
e[i][1] = e[i][0];
e[i][0] = (int)(w[i] * 4095. / 83.77580409572) - axis[i];

u[i][0] = u[i][1] + Kp[i]*(e[i][0] - e[i][1]);// + Ki[i]*Ts*(e[i][0]) + (Kd[i]/Ts)*(e[i][0] - 2*e[i][1] + e[i][2])



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

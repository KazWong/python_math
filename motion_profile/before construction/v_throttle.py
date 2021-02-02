import matplotlib.pyplot as plt
import numpy as np
import math

MAX_ACC = 2.37551
MIN_ACC = 0.1
h = 0.01
N = 100.

T = N*h
a = [0.0, 0.0, 0.0, 0.0]
a[0] = 0.0
a[1] = MIN_ACC*h
a[2] = (MAX_ACC - MIN_ACC)*h / (2*N)
a[3] = 0.0

### Plot ###
t1 = np.linspace(0, T, T+1)
t2 = t1*t1
t3 = t2*t1

pos  = 0 + a[0]*t1 + a[1]*t2/2 + a[2]*t2/3 + a[3]*t3/4
vel  = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3
acc  = a[1] + 2*a[2]*t1 + 3*a[3]*t2
jerk = 2*a[2] + 6*a[3]*t1

for i in range(4):
  print('a[', i ,'] = ', a[i])

print(a[1] + 2*a[2]*t1[0] + 3*a[3]*t2[0], a[1] + 2*a[2]*t1[-1] + 3*a[3]*t2[-1])

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

import numpy as np
import matplotlib.pyplot as plt
from ..motion_profile.linear import XVAJ
from ..simtools import *
from ..simtools.plotlib import *

sampling_rate = 1000.
clock = Time(1./sampling_rate)

shift = 0.0;end_time = 5.

x0 = [0., 0., 0., 0.]
xn= [0.7, 0.5, 0., 0.]
vmax = 0.4
T = 4.0 #(xn[0] - x0[0])/(vmax**2)


x = XVAJ(T, x0, xn)
print('a: ', x.a())
print('T: ', T)

clock.Reset()
clock.Offline(shift)
while (clock.now() < end_time):
    clock.Tick()
    x.Update()

y = x.Y()
y = y.reshape([-1, 4])

plt.figure()
plt.suptitle('xvaj')
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(x.timespace(), y[:,0], label='vaj, t shift: ' + str(shift))
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(x.timespace(), y[:,1], label='vaj, t shift: ' + str(shift))
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(x.timespace(), y[:,2], label='vaj, t shift: ' + str(shift))
plt.subplot(414)
plt.ylabel('jerk')
plt.plot(x.timespace(), y[:,3], label='vaj, t shift: ' + str(shift))


plt.show()

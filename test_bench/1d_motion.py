import numpy as np
import matplotlib.pyplot as plt
from ..dynamic_systems.motion import Translation1D
from ..motion_profile.vaj import Motion_vaj
#from ..dynamic_systems.dry_air import DryAir
from ..simtools import *

sampling_rate = 1000.
clock = Time(1./sampling_rate)

x0 = [0., 0., 0., 0.]
xn1 = [5., 0., 0.]
xn = [-3., 0., 0.]
T1 = 10.
T2 = 36.

obj = Translation1D(x0)
u0 = Motion_vaj(T1, x0[1:], xn1)
u = [0.0, 0.0, 0.0]
u_1 = [0.0, 0.0, 0.0]

clock.Reset()
while (clock.now() < T1):
    clock.Tick()
    u_1 = u0.Update()
    obj.Update( np.array([u_1 - u]) )
    u = u_1

x0 = obj.y()
u1 = Motion_vaj(T2-T1, x0[1:], xn)
u1.t_shift(-clock.now())
while (clock.now() < T2):
    clock.Tick()
    u_1 = u1.Update()
    obj.Update( np.array([u_1 - u]) )
    u = u_1

y = obj.Y()
y = y.reshape([-1, 4])

pos = u0.Pos()
pos = np.append(pos, u1.Pos())
t = u0.timespace()
t = np.append(t, u1.timespace())

plt.suptitle('1D Motion')
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(clock.timespace(), y[:,0])
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(clock.timespace(), y[:,1])
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(clock.timespace(), y[:,2])
plt.subplot(414)
plt.xlabel('t')
plt.ylabel('jerk')
plt.plot(clock.timespace(), y[:,3])

plt.show()

import numpy as np
import matplotlib.pyplot as plt
#from ..dynamic_systems.damped_sinusoidal_oscillator import DampedSinOsc
from ..dynamic_systems.motion import Translation1D
#from ..dynamic_systems.dry_air import DryAir
from ..simtools import *
from ..simtools.gaussian import LinearGaussian, SineGaussian

sampling_rate = 1000.;end_time = 5.
clock = Time(1.)


### Translation1D
x0 = [0., 5., 0., 0.]
i = 0
u = np.array([[5., 0., 0.],
    [4., 0., 0.],
    [3., 0., 0.],
    [2., 0., 0.],
    [1., 0., 0.],
    [0., 0., 0.]])

x = Translation1D(x0)
clock.Reset()
while (clock.now() < end_time):
    clock.Tick()
    x.Update(np.array([u[i]]))
    if (i < 5):
        i += 1
off_motion = x.Y()
off_motion = off_motion.reshape([-1, 4])

plt.figure()
plt.subplot(311)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(clock.timespace(), off_motion[:,0], c='r', s=0.5)
plt.scatter(clock.timespace(), off_motion[:,1], c='g', s=0.5)
#plt.scatter(clock.timespace(), off_motion[:,2], c='b', s=0.5)


"""
### Dry Air
time = 5;sigma = 0.01;volume = 1.;temperature = 25.5
disturbance = LinearGaussian(clock, 0., 10., 5.)
measurement_noise = LinearGaussian(clock, 3., 0., 0.)
dry_air = DryAir(clock, volume, temperature, disturbance, measurement_noise)
off_dry_air = dry_air.Offline(end_time)

plt.subplot(312)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(clock.timespace, off_dry_air, c='g', s=0.5)


### Damped Sinusoid
damping_ratio = 0.1;amp = 10.;frq = 2.;shift = 0.
damp = DampedSinOsc(clock, damping_ratio, amp, frq, shift)
off_damp = damp.Offline(end_time)

plt.subplot(313)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(clock.timespace, off_damp, c='g', s=0.5)
"""

plt.show()

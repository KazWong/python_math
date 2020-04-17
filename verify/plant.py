import numpy as np
import matplotlib.pyplot as plt
from ..dynamic_systems.damped_sinusoidal_oscillator import DampedSinOsc
from ..dynamic_systems.newtonian import Newtonian
from ..dynamic_systems.dry_air import DryAir
from ..signal import Ideal, Time
from ..signal.sine_gaussian import SineGaussian
from ..signal.linear_gaussian import LinearGaussian

sampling_rate = 1000.;end_time = 4.
clock = Time(sampling_rate)


### Newtonian
X0 = [0., 5., -10, 0.];sigma = 0.2;A = 0.0001;f = 1.;m = 0.;c = 0.
di = [Ideal(),
      Ideal(),
      SineGaussian(clock, sigma, A, f),
      Ideal()]
do = [LinearGaussian(clock, sigma, m, c),
      LinearGaussian(clock, sigma, m, c),
      Ideal(),
      Ideal()]    
motion = Newtonian( clock, X0, di=di, do=do )
off_motion = motion.Offline(end_time)
off_motion = off_motion.reshape([-1, 4])

plt.subplot(311)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(clock.timespace, off_motion[:,0], c='r', s=0.5)
plt.scatter(clock.timespace, off_motion[:,1], c='g', s=0.5)
plt.scatter(clock.timespace, off_motion[:,2], c='b', s=0.5)


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


plt.show()

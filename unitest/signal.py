import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from ..signal import Signal, Ideal, Time
from ..signal.linear_gaussian import LinearGaussian
from ..signal.sine_gaussian import SineGaussian
from ..signal.pulse import Impulse, Square, PWM

sampling_rate = 1000.;end_time = 4.
clock = Time(sampling_rate, end_time)

if (clock.Hz() != sampling_rate): raise AssertionError()
if (clock.T() != 1./sampling_rate): raise AssertionError()
if (clock.timespace[0] != 0.): raise AssertionError()
if (clock.timespace[-1] != end_time): raise AssertionError()
tick = np.around([clock.Tick() for _ in clock.range], 3)
timespace = np.around(clock.timespace, 3)
if ( tick != timespace ).any(): raise AssertionError()
clock.Reset()
tick = np.around([clock.Tick() for _ in range(int(sampling_rate*2*end_time)+1)], 3)
timespace = np.around(clock.timespace, 3)
if (clock.timespace[0] != 0.): raise AssertionError()
if (clock.timespace[-1] != 2*end_time): raise AssertionError()
clock.Reset()

sigma = 0.0;m = 1.;c = 1.
y = np.around(np.linspace(c, m*end_time+c, clock.len), 3)
yl = np.around(LinearGaussian(clock, sigma, m, c).Offline(), 3)
if (y != yl).any(): raise AssertionError()

plt.subplot(511)
plt.plot(clock.timespace, yl)
plt.title("Linear")


amp = 1.;frq = 1.;shift = 0.
t = np.linspace(0., end_time, clock.len)
y = np.around(np.array( amp*np.sin(2.*math.pi*frq*t+shift) ), 3)
ys = np.around(SineGaussian(clock, sigma, amp, frq, shift).Offline(), 3)
if (y != ys).any(): raise AssertionError()

plt.subplot(512)
plt.plot(clock.timespace, y)
plt.title("Sine")


terms = 40;amp = 2.;frq = 1.
y = Square(clock, sigma, terms, amp, frq).Offline()

plt.subplot(513)
plt.plot(clock.timespace, y)
plt.title("Sine Square")


max_A = 2.;min_A = 0.;frq = 1.;shift = frq/2.
y = PWM(clock, max_A, min_A, frq, shift=shift).Offline()

plt.subplot(514)
plt.plot(clock.timespace, y)
plt.title("PWM")


t = 4.;A = 4.5
#y = Impulse(clock, t, A).Offline()

#plt.subplot(515)
#plt.plot(clock.timespace, y)
#plt.title("Impulse")


plt.show()

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from ..signal import Signal, Ideal, Time
from ..signal.linear_gaussian import LinearGaussian
from ..signal.sine_gaussian import SineGaussian
from ..signal.pulse import Square, PWM

sampling_rate = 1000.;end_time = 4.
clock = Time(sampling_rate)



sigma = 0.2;m = 1.;c = 1.
y = np.around(np.linspace(c, m*end_time+c, clock.Len()), 3)
yl = np.around(LinearGaussian(clock, 0.0, m, c).Offline(), 3)
yl2 = LinearGaussian(clock, sigma, m, c).Offline()
if (y != yl).any(): raise AssertionError()

plt.subplot(511)
plt.scatter(clock.timespace, yl2, c='g', s=0.5)
plt.plot(clock.timespace, yl)
plt.title("Linear")


amp = 1.;frq = 1.;shift = 0.
t = np.linspace(0., end_time, clock.Len())
y = np.around(np.array( amp*np.sin(2.*math.pi*frq*t+shift) ), 3)
ys = np.around(SineGaussian(clock, 0.0, amp, frq, shift).Offline(), 3)
ys2 = np.around(SineGaussian(clock, sigma, amp, frq, shift).Offline(), 3)
if (y != ys).any(): raise AssertionError()

plt.subplot(512)
plt.scatter(clock.timespace, ys2, c='g', s=0.5)
plt.plot(clock.timespace, ys)
plt.title("Sine")


terms = 40;amp = 4.;frq = 4.
y = Square(clock, 0.0, terms, amp, frq).Offline()
y2 = Square(clock, sigma, terms, amp, frq).Offline()

plt.subplot(513)
plt.scatter(clock.timespace, y2, c='g', s=0.5)
plt.plot(clock.timespace, y)
plt.title("Sine Square")


terms = 40;amp = 4.;frq = 1.;d = 0.2
y = PWM(clock, 0.0, terms, amp, frq, d).Offline()
yw = PWM(clock, sigma, terms, amp, frq, d).Offline()

plt.subplot(514)
plt.plot(clock.timespace, y)
plt.scatter(clock.timespace, yw, c='g', s=0.5)
plt.title("PWM")


plt.show()

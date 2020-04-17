import numpy as np
import math
import matplotlib.pyplot as plt
from ..signal import Signal, Ideal, Time
from ..signal.linear_gaussian import LinearGaussian
from ..signal.sine_gaussian import SineGaussian
from ..signal.pulse import Square, PWM

sampling_rate = 1000.;end_time = 4.
clock = Time(sampling_rate)

# step verify
l = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
c = Time(10).Offline(1.0)
if (c != l).any(): 
  print(c != l)
  print(c)
  print(l)
  raise AssertionError()
l = np.array([0.0, 0.090909, 0.181818, 0.272727, 0.363636, 0.454545, 0.545455, 0.636364, 0.727273, 0.818182, 0.909091, 1.0])
c = np.around( Time(11).Offline(1.0), 6)
if (c != l).any(): 
  print(c)
  print(l)
  raise AssertionError()
l = np.array([0.0, 0.111111, 0.222222, 0.333333, 0.444444, 0.555556, 0.666667, 0.777778, 0.888889, 1.0])
c = np.around( Time(9).Offline(1.0), 6)
if (c != l).any(): 
  print(c)
  print(l)
  raise AssertionError()


# Offline Signal test
clock.Offline(end_time)

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


terms = 40;amp = 4.;frq = 4.;shift = math.pi/3
y = Square(clock, 0.0, terms, amp, frq, shift).Offline()
y2 = Square(clock, sigma, terms, amp, frq, shift).Offline()

plt.subplot(513)
plt.scatter(clock.timespace, y2, c='g', s=0.5)
plt.plot(clock.timespace, y)
plt.title("Sine Square")


terms = 80;amp = 4.;frq = 4.;d = 0.5;shift = 0.
y = PWM(clock, 0.0, terms, amp, frq, d, shift).Offline()
yw = PWM(clock, sigma, terms, amp, frq, d, shift).Offline()

plt.subplot(514)
plt.plot(clock.timespace, y)
plt.scatter(clock.timespace, yw, c='g', s=0.5)
plt.title("PWM")


plt.show()

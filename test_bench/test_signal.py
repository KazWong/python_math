import numpy as np
import math
import matplotlib.pyplot as plt
from ..signal import Signal, Ideal, Time
from ..signal.linear_gaussian import LinearGaussian
from ..signal.sine_gaussian import SineGaussian
from ..signal.pulse import Square, PWM

sampling_rate = 1000.;end_time = 4.
clock = Time(sampling_rate)

#Offline time
clock.Offline(end_time)
if (clock.Hz() != sampling_rate): raise AssertionError()
if (clock.T() != 1./sampling_rate): raise AssertionError()
if (clock.timespace[0] != 0.): raise AssertionError()
if (clock.timespace[-1] != end_time):
  print(clock.timespace[-1]) 
  print(end_time[-1]) 
  raise AssertionError()
clock.Reset()

#Tick time and timespace consistency
tick = np.array([])
for i in range(int(sampling_rate*end_time)+1):
  tick = np.append(tick, np.around(clock.Tick(), 3) )
timespace = np.around(clock.timespace, 3)
if (tick[0] != timespace[0]) or (tick[0] != 0.0): 
  print(timespace[0])
  print(tick[0])
  raise AssertionError()
if (tick[-1] != timespace[-1]) or (tick[-1] != end_time):
  print(timespace[-1])
  print(tick[-1])
  print(end_time)
  raise AssertionError()
if (tick.size != timespace.size):
  raise AssertionError()
if ( tick != timespace ).any(): 
  raise AssertionError()
clock.Reset()

#Tick after Offline
clock.Offline(end_time)
tick = clock.timespace
for i in range(int(sampling_rate*end_time)+1, int(sampling_rate*2*end_time)+1):
  tick = np.append(tick, np.around(clock.Tick(), 3) )
timespace = np.around(clock.timespace, 3)
if (clock.timespace[0] != 0.): raise AssertionError()
if (clock.timespace[-1] != 2*end_time): 
  print(clock.timespace[-1])
  print(2*end_time)
  raise AssertionError()
clock.Reset()


#Offline Signal test
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

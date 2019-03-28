import numpy as np
import matplotlib.pyplot as plt
from ..plant.damped_sinusoidal_oscillator import DampedSinOsc

_sample_rate = 1000
time = 5
sigma = 0.01
amp = 10.
frq = 2.
shift = 0.
t, p_x = DampedSinOsc(_sample_rate, 0.1, amp, frq, shift).Offline(time)

plant = DampedSinOsc(_sample_rate, 0.1, amp, frq, shift)
for _ in range(len(p_x)):
  plant.Online()


plt.subplot(121)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(t, p_x, c='g', s=0.5)

plt.subplot(122)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(t, plant.x, c='g', s=0.5)

plt.show()

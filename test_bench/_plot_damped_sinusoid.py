import numpy as np
import matplotlib.pyplot as plt
from ..plant.damped_sinusoidal_oscillator import DampedSinOsc

resolution = 1000
time = 5
sigma = 0.01
amp = 10.
frq = 2.
shift = 0.
p_x, p_y = DampedSinOsc(resolution, 0.1, amp, frq, shift).Offline(time)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g', s=0.7)
plt.show()

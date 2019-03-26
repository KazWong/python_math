import numpy as np
import matplotlib.pyplot as plt
from ..signal.sine_gaussian import SineGaussian

resolution = 1000
time = 5
sigma = 0.01
amp = 1.
frq = 0.5
shift = 0.
p_x, p_y = SineGaussian(sigma, amp, frq, shift).Offline(time, resolution)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.show()

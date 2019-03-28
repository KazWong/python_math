import numpy as np
import matplotlib.pyplot as plt
from ..signal.sine_gaussian import SineGaussian

resolution = 1000
time = 5
sigma = 0.0
amp = 1.
frq = 1.
shift = 0.
p_x, p_y = SineGaussian(sigma, amp, frq, shift).Offline(time, resolution)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g', s=0.5)
plt.show()

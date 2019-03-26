import numpy as np
import matplotlib.pyplot as plt
from ..signal.linear_gaussian import LinearGaussian

resolution = 5
time = 5
sigma = 1.3
o_m = 0.
o_c = 1.
p_x, p_y = LinearGaussian(sigma, o_m, o_c).Offline(time, resolution)
o_y = o_m*p_x+o_c

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.plot(p_x, o_y, 'r--')
plt.show()

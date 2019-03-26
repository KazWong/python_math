import numpy as np
import matplotlib.pyplot as plt
from ..plant.motion import Motion
from ..signal.linear_gaussian import LinearGaussian

resolution = 1000
time = 5
sigma = 0.01
A0 = [1., 1., 1., 1.]
disturbance = LinearGaussian(0., 0., 0.)
measurement_noise = LinearGaussian(0., 0., 0.)
p_x, p_y = Motion(resolution, A0, disturbance, measurement_noise).Offline(time)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g', s=0.5)
plt.show()

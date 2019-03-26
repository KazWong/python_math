import numpy as np
import matplotlib.pyplot as plt
from ..plant.dry_air import DryAir
from ..signal.linear_gaussian import LinearGaussian

resolution = 1000
time = 5
sigma = 0.01
volume = 1.
temperature = 25.5
disturbance = LinearGaussian(0., 10., 5.)
measurement_noise = LinearGaussian(3., 0., 0.)
p_x, p_y = DryAir(resolution, volume, temperature, disturbance, measurement_noise).Offline(time)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g', s=0.5)
plt.show()

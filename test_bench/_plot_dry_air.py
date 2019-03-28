import numpy as np
import matplotlib.pyplot as plt
from ..plant.dry_air import DryAir
from ..signal.linear_gaussian import LinearGaussian

_sample_rate = 1000
time = 5
sigma = 0.01
volume = 1.
temperature = 25.5
disturbance = LinearGaussian(0., 10., 5.)
measurement_noise = LinearGaussian(3., 0., 0.)

plant = DryAir(_sample_rate, volume, temperature, disturbance, measurement_noise)
t, p_x = plant.Offline(time)

plant2 = DryAir(_sample_rate, volume, temperature, disturbance, measurement_noise)
for _ in range(len(p_x)):
  plant2.Online(0.)


plt.subplot(121)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(t, p_x, c='g', s=0.5)

plt.subplot(122)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(t, plant2.x, c='g', s=0.5)

plt.show()

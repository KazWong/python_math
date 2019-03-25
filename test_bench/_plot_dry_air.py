import numpy as np
import matplotlib.pyplot as plt
from ..plant.dry_air import DryAir

resolution = 1000
time = 5
sigma = 0.01
volume = 1.
temperature = 25.5
p_x, p_y = DryAir(resolution, volume, temperature).Offline(time)

plt.subplot(111)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(p_x, p_y, c='g')
plt.show()

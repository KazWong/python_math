import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.dry_air import DryAir
from ..plant.linear_gaussian import LinearGaussian

disturbance = LinearGaussian(1.3, 0.1, -0.1)
plant = DryAir(10, 1, 25, disturbance)

for i in xrange(1000):
  plant.Online(-100)

plt.subplot(111)
plt.xlabel('t')
plt.ylabel('y')
plt.scatter(plant.t, plant.y, c='g')
plt.show()

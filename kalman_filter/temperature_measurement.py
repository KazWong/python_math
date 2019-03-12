import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.dry_air import DryAir

plant = DryAir(10, 1, 25)

for i in xrange(100):
  plant.Online(10)

plt.subplot(111)
plt.xlabel('t')
plt.ylabel('y')
plt.scatter(plant.t, plant.y, c='g')
plt.show()

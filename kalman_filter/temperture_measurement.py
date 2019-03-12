import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.linear_gaussian import LinearGaussian

t, y = LinearGaussian(10, 0.6, 0, 25).Offline(5)

plt.subplot(111)
plt.xlabel('t')
plt.ylabel('y')
plt.scatter(t, y, c='g')
plt.show()

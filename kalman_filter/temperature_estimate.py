import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.dry_air import DryAir
from ..plant.linear_gaussian import LinearGaussian

plant = DryAir( 10, 1, 25, LinearGaussian(0.6, 0., 0.5) )

Kalman = [20.]
Er_est = [2.]
Mea = []
Er_Mea = [1.]
Kg = 1.
for i in xrange(1000):
  t, y = plant.Online(0)
  
  Mea.append(y)
  Kg = Er_est[-1] / (Er_est[-1] + Er_Mea[-1])
  Kalman.append( Kalman[-1] + Kg * (Mea[-1] - Kalman[-1]) )
  Er_est.append( (1 - Kg) * Er_est[-1] )

plt.subplot(111)
plt.xlabel('t')
plt.ylabel('y')
plt.scatter(plant.t, plant.y, c='g')
plt.plot(plant.t, Kalman)
plt.plot(plant.t, Er_est)
plt.show()

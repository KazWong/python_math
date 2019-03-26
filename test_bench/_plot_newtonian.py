import numpy as np
import matplotlib.pyplot as plt
from ..plant.newtonian import Newtonian
from ..signal.linear_gaussian import LinearGaussian

_sample_rate = 100
time = 5
sigma = 0.01
A0 = [0., 10., -9.81, 0.]
disturbance = LinearGaussian(0., 0., 0.)
measurement_noise = LinearGaussian(0., 0., 0.)

plant = Newtonian(_sample_rate, A0, disturbance, measurement_noise)
p_x, p_y = plant.Offline(time)

plant2 = Newtonian(_sample_rate, A0, disturbance, measurement_noise)
p_x2 = 0.
p_y2 = np.array([])


while (round(p_x2, 3) < time):
  p_x2, _ = plant2.Online([0.])
p_y2 = plant2.x.reshape([-1, 4])


plt.subplot(421)
plt.xlabel('t')
plt.ylabel('pos')
plt.scatter(p_x, p_y[:,0], s=0.5)
plt.subplot(423)
plt.xlabel('t')
plt.ylabel('vel')
plt.scatter(p_x, p_y[:,1], s=0.5)
plt.subplot(425)
plt.xlabel('t')
plt.ylabel('acc')
plt.scatter(p_x, p_y[:,2], s=0.5)
plt.subplot(427)
plt.ylabel('jerk')
plt.scatter(p_x, p_y[:,3], s=0.5)

plt.subplot(422)
plt.xlabel('t')
plt.ylabel('Online pos')
plt.scatter(p_x, p_y2[:,0], s=0.5)
plt.subplot(424)
plt.xlabel('t')
plt.ylabel('Online vel')
plt.scatter(p_x, p_y2[:,1], s=0.5)
plt.subplot(426)
plt.xlabel('t')
plt.ylabel('Online acc')
plt.scatter(p_x, p_y2[:,2], s=0.5)
plt.subplot(428)
plt.ylabel('Online jerk')
plt.scatter(p_x, p_y2[:,3], s=0.5)

plt.show()

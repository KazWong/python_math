import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.newtonian import Newtonian
from ..signal.linear_gaussian import LinearGaussian
from ..kalman_filter.kalman_filter import KalmanFilter

A = [0. 5. -9.81 0.]
sample_rate = 100.
plant = Newtonian( sample_rate, 1, vol, init_temp, _do=LinearGaussian(1.3, 0., 0.) )

A = [1.]
X = [20.] # State
P = [1.] # Process covariance matrix
B = [1./(1005.*plant.Density(init_temp)*vol*sample_rate)]
u = [] # control variable matrix
w = [0.] # Process noise
Q = [1./sample_rate] # Process noise covariance matrix
Y = [] # Observation
Z = [0.] # Observation noise
R = [1.] # Observation noise covariance matrix
K = [1.] # Kalman gain


plt.subplot(111)
plt.xlabel('t')
plt.ylabel('y')
plt.plot(plant.t, plant.y, 'r--', linewidth=0.5)
plt.plot(plant.t, X)
plt.plot(plant.t, K)
plt.plot(plant.t, true_y)
plt.show()

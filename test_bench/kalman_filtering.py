import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.newtonian import Newtonian
from ..signal.linear_gaussian import LinearGaussian
from ..bayesian_filtering.kalman_filter import KalmanFilter

X0 = [0., 5., 0., 0.]
sample_rate = 1000.
plant = Newtonian( sample_rate, X0, _do=LinearGaussian(1.3, 0., 0.) )
kf = KalmanFilter(1./sample_rate)

A = [1.]
X = [20.] # State
P = [1.] # Process covariance matrix
B = []
u = [] # control variable matrix
w = [0.] # Process noise
Q = [] # Process noise covariance matrix
Y = [] # Observation
Z = [0.] # Observation noise
R = [1.] # Observation noise covariance matrix
K = np.array([]) # Kalman gain
P = np.array([]) # variance

z = np.array([])

for i in range(500):
  _, X = plant.Online([0.])
  kf.Predict([0.])
  kf.Update(X[0])
  
  K = np.append(K, kf.K)
  P = np.append(P, kf.P)
  z = np.append( z, kf.X )

zz = z.reshape([-1, 2])
p_y2 = plant.x.reshape([-1, 4])
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(plant.t, zz[:,0], 'r')
plt.scatter(plant.t, p_y2[:,0], s=0.5)

plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(plant.t, zz[:,1], 'r')
plt.scatter(plant.t, p_y2[:,1], s=0.5)

KK = K.reshape([-1, 2])
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('Kalman gain')
plt.scatter(plant.t, KK[:,0], s=0.5, c='g')
plt.scatter(plant.t, KK[:,1], s=0.5, c='b')

PP = P.reshape([-1, 4])
plt.subplot(414)
plt.ylabel('Variance')
plt.scatter(plant.t, PP[:,0], s=0.5, c='g')
plt.scatter(plant.t, PP[:,3], s=0.5, c='b')

plt.show()

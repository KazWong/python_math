import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.newtonian import Newtonian
from ..signal.signal import Ideal
from ..signal.sine_gaussian import SineGaussian
from ..signal.linear_gaussian import LinearGaussian
from ..bayesian_filtering.kalman_filter import KalmanFilter

X0 = [0., 5., -9.81, 0.]
sample_rate = 100.

di = [SineGaussian(1.1, 10., 1.),
      LinearGaussian(0.0, 0., 0.),
      Ideal(),
      Ideal()]
do = [LinearGaussian(1.1, 0., 0.),
      LinearGaussian(1.1, 0., 0.),
      Ideal(),
      Ideal()]
      
plant = Newtonian( sample_rate, X0, _di=di, _do=do )
kf = KalmanFilter()
T = 1./sample_rate

#parameters
kf.F = np.array([[1., T], [0, 1.]])
kf.X = np.array([[0.], [4.5]])
kf.B = np.array([[0.5*T**2], [T]])
kf.P = np.array([[50., 0], [0, 50.]])
kf.Q = np.array([[0.1, 0], [0, 0.1]])
kf.R = np.array([[2., 0], [0, 2.0]])
kf.Init([1., 1])

#var
x = np.array([])
K = np.array([])
P = np.array([])

for i in range(500):
  _, X = plant.Online([0., 0., 0.005, 0.])
  kf.Predict([0.005])
  kf.Update(X[:2])
  
  K = np.append(K, kf.K)
  P = np.append(P, kf.P)
  x = np.append(x, kf.X)

x = x.reshape([-1, 2])
z = plant.x.reshape([-1, 4])
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(plant.t, x[:,0], 'r')
plt.scatter(plant.t, z[:,0], s=0.5)
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(plant.t, x[:,1], 'r')
plt.scatter(plant.t, z[:,1], s=0.5)

K = K.reshape([-1, 4])
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('Kalman gain')
plt.scatter(plant.t, K[:,0], s=0.5, c='g')
plt.scatter(plant.t, K[:,3], s=0.5, c='b')

P = P.reshape([-1, 4])
plt.subplot(414)
plt.ylabel('Variance')
plt.scatter(plant.t, P[:,0], s=0.5, c='g')
plt.scatter(plant.t, P[:,3], s=0.5, c='b')

plt.show()

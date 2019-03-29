import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.newtonian import Newtonian
from ..signal import Ideal, Time
from ..signal.sine_gaussian import SineGaussian
from ..signal.linear_gaussian import LinearGaussian
from ..bayesian_filtering.kalman_filter import KalmanFilter

#Clock
sampling_rate = 1000.;end_time = 2.
clock = Time(sampling_rate)

#plant
X0 = [0., 5., -10, 0.]
di = [Ideal(),
      Ideal(),
      SineGaussian(clock, 0.0, 0., 0.),
      Ideal()]
do = [LinearGaussian(clock, 1.3, 0., 0.),
      LinearGaussian(clock, 1.3, 0., 0.),
      Ideal(),
      Ideal()]    
plant = Newtonian( clock, X0, di=di, do=do )

#Kalman filter
kf = KalmanFilter()
T = clock.T()
kf.F = np.array([[1., T], [0, 1.]])
kf.X = np.array([[0.], [4.5]])
kf.B = np.array([[0.5*T**2], [T]])
kf.P = np.array([[50., 0], [0, 50.]])
kf.Q = np.array([[0.01, 0], [0, 0.01]])
kf.R = np.array([[0.2, 0], [0, 0.2]])
kf.Init([1., 1])

#var
x = np.array([])
K = np.array([])
P = np.array([])
u = [0., 0., 0., 0.]

for i in clock.Range(end_time):
  X = plant.Online(u)
  kf.Predict([u[2]])
  kf.Update(X[:2])
  clock.Tick()
  
  K = np.append(K, kf.K)
  P = np.append(P, kf.P)
  x = np.append(x, kf.X)

x = x.reshape([-1, 2])
z = plant.x.reshape([-1, 4])
plt.subplot(511)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(clock.timespace, x[:,0], 'r')
plt.scatter(clock.timespace, z[:,0], s=0.5)
plt.subplot(512)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(clock.timespace, x[:,1], 'r')
plt.scatter(clock.timespace, z[:,1], s=0.5)
plt.subplot(513)
plt.xlabel('t')
plt.ylabel('acc')
plt.scatter(clock.timespace, z[:,2], s=0.5)


K = K.reshape([-1, 4])
plt.subplot(514)
plt.xlabel('t')
plt.ylabel('Kalman gain')
plt.scatter(clock.timespace, K[:,0], s=0.5, c='g')
plt.scatter(clock.timespace, K[:,3], s=0.5, c='b')


P = P.reshape([-1, 4])
plt.subplot(515)
plt.ylabel('Variance')
plt.scatter(clock.timespace, P[:,0], s=0.5, c='g')
plt.scatter(clock.timespace, P[:,3], s=0.5, c='b')

plt.show()

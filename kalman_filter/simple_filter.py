import math
import numpy as np
import random
import matplotlib.pyplot as plt
from ..plant.dry_air import DryAir
from ..plant.linear_gaussian import LinearGaussian

vol = 1.
init_temp = 25.
sample_rate = 10.
plant = DryAir( sample_rate, vol, init_temp, LinearGaussian(0., 0., 0.), LinearGaussian(0.6, 0., 0.) )

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

total_measurement = []
true_y = [25.]
var = 0.

#without error covariance
for i in xrange(200):
  u.append(0.)
  t, y = plant.Online(u[-1])
  true_y.append( plant._T )
  
  #process convariance
  total_measurement.append(y)
  var = (sum(total_measurement)/len(total_measurement) - y) + var
  
  #Prediced state
  Xp = A[-1]*X[-1] + B[-1]*u[-1] + w[-1]
  P.append( pow(var/len(total_measurement), 2) + Q[-1] )
  #Measurement state
  K.append( P[-1] / (P[-1] + R[-1]) )
  Y.append( y + Z[-1] )
  X.append( Xp + K[-1]*(Y[-1] - X[-1]) )
  #Current state
  P.append( K[-1]*P[-1] )

plt.subplot(111)
plt.xlabel('t')
plt.ylabel('y')
plt.plot(plant.t, plant.y, 'r--', linewidth=0.5)
plt.plot(plant.t, X)
plt.plot(plant.t, K)
plt.plot(plant.t, true_y)
plt.show()

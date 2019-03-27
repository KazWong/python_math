import math
import numpy as np
  
  #process convariance
  total_measurement.append(y)
  var = (sum(total_measurement)/len(total_measurement) - y) + var

class KalmanFilter:
  def __init__(self, A, X, P, B, u, w, Q, Y, Z, R):
    self.A = [1.]
    self.X = [20.] # State
    self.P = [1.] # Process covariance matrix
    self.B = [1./(1005.*plant.Density(init_temp)*vol*sample_rate)]
    self.u = [] # control variable matrix
    self.w = [0.] # Process noise
    self.Q = [1./sample_rate] # Process noise covariance matrix
    self.Y = [] # Observation
    self.Z = [0.] # Observation noise
    self.R = [1.] # Observation noise covariance matrix
    self.K = [1.] # Kalman gain
    
  def Predict():
    #Prediced state
    Xp = A[-1]*X[-1] + B[-1]*u[-1] + w[-1]
    P.append( pow(var/len(total_measurement), 2) + Q[-1] )
  
  def Update():
    #Measurement state
    K.append( P[-1] / (P[-1] + R[-1]) )
    Y.append( y + Z[-1] )
    X.append( Xp + K[-1]*(Y[-1] - X[-1]) )
    #Current state
    P.append( K[-1]*P[-1] )

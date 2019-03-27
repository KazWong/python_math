import math
import numpy as np

class KalmanFilter:
  def __init__(self):
    self.F = np.array([]) # state transition matrix
    self.X = np.array([]) # State
    self.B = np.array([]) # control input model
    self.u = np.array([]) # control input matrix
    self.w = np.array([]) # Process noise
    self.P = np.array([]) # Process covariance matrix
    self.Q = np.array([]) # Process noise covariance matrix
    self.Z = np.array([]) # Observation noise
    self.R = np.array([]) # Observation noise covariance matrix
    self.K = np.array([]) # Kalman gain
    
    self.I = np.array([])
    self.H = np.array([])
  
  def Init(self, _z):
    z = np.array(_z)
    self.I = np.eye(self.P.shape[0])
    
    if (self.w.size == 0):
      self.w = np.array([[0.] * self.X.shape[0]]).T
      
    if (self.Z.size == 0):
      self.Z = np.array([[0.] * z.size]).T
  
    zb = z!=0.
    H = np.zeros((zb.size, self.X.size))
    for i in range(zb.size):
      H[i, i] = float(zb[i])
    self.H = H[:]
  
  
  def Predict(self, u):
    #Prediced state
    self.Xp = np.dot(self.F, self.X) + self.B.dot(np.array([u])) + self.w
    self.Pp = self.F.dot(self.P).dot(self.F.T) + self.Q
  
  
  def Update(self, z):
    #Measurement state
    PpH_T = self.Pp.dot(self.H.T)
    self.K = PpH_T.dot( np.linalg.inv(self.H.dot(PpH_T) + self.R) )
    self.Y = np.array([z]).T - self.H.dot(self.Xp) + self.Z
    self.X = self.Xp + self.K.dot(self.Y)
    self.P = ( self.I - self.K.dot(self.H) ).dot(self.Pp)

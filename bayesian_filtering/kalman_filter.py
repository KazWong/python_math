import math
import numpy as np

class KalmanFilter:
  def __init__(self, T, F=0, X=0, B=0, u=0, w=0, P=0, Q=0, R=0, Z=0, H=0):
    self.F = np.array([[1., T], [0, 1.]])
    self.X = np.array([[0.], [4.5]]) # State
    self.B = np.array([[0.5*T**2], [T]])
    self.u = np.array([[0.]]) # control variable matrix
    self.w = np.array([[0.], [0]]) # Process noise
    self.P = np.array([[50., 0], [0, 50.]]) # Process covariance matrix
    self.Q = np.array([[0., 0], [0, 0.01]]) # Process noise covariance matrix
    self.H = np.array([[1., 0.]])
    self.Z = np.array([[0.]]) # Observation noise
    self.R = np.array([[1.69]]) # Observation noise covariance matrix
    self.I = np.eye(2)
    
  def Predict(self, u):
    #Prediced state
    self.Xp = np.dot(self.F, self.X) + self.B.dot(np.array([u])) + self.w
    self.Pp = self.F.dot(self.P).dot(self.F.T) + self.Q
  
  def Update(self, z):
    #Measurement state
    PpH_T = self.Pp.dot(self.H.T)
    self.K = PpH_T.dot( np.linalg.inv(self.H.dot(PpH_T) + self.R) )
    self.Y = np.array([z]) - self.H.dot(self.Xp) + self.Z
    self.X = self.Xp + self.K.dot(self.Y)
    self.P = ( self.I - self.K.dot(self.H) ).dot(self.Pp)

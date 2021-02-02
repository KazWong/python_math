import math
import numpy as np

class KalmanFilter:
  def __init__(self):
    pass
  
  def Init(self, _z):
    pass
  
  def Predict(self, muc, covc):
    #Prediced state
    self.mup = self.mu + muc
    self.covp = self.cov + self.covc
  
  def Update(self, muz, covz):
    #Measurement state
    cov_sum = np.linalg.inv(self.covp + covz)
    self.mu = covz.dot(cov_sum).dot(self.mup) + self.covp.dot(cov.sum).dot(muz)
    self.cov = self.covp.dot(cov_sum).dot(covz)
    
    

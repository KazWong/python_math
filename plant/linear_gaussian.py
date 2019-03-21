import numpy as np
import random
from .disturbance import Disturbance

class LinearGaussian(Disturbance):
  def __init__(self, _sigma, _m, _c):
    super(LinearGaussian, self).__init__()
  
    self.sig = float(_sigma)
    self.m = float(_m)
    self.c = float(_c)
    self.t = 0.
    
  def Model(self, t):
    return random.gauss(self.m * t + self.c, self.sig)
  
  def Reset(self, _m, _c):
    self.m = float(_m)
    self.c = float(_c)
    
  def Offline(self, end_t, sample_rate):
    sample = float(end_t) * sample_rate;
    t = np.linspace(0., end_t, sample, endpoint=True)
    y = np.array([self.Model(t[_]) for _ in range(int(sample))])
    
    return t, y
  
  def Online(self, t):
    return self.Model(t)

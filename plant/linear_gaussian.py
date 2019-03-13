import numpy as np
import random
from disturbance import Disturbance

class LinearGaussian(Disturbance):
  def __init__(self, _sigma, _m, _c):
    super(LinearGaussian, self).__init__()
  
    self.sig = float(_sigma)
    self.m = float(_m)
    self.c = float(_c)
    self.t = 0.
  
  def Reset(self, _m, _c):
    self.m = float(_m)
    self.c = float(_c)
    
  def Offline(self, end_t, sample_rate):
    t = []
    y = []
    
    sample = float(end_t) * sample_rate;
    t = np.linspace(0., end_t, sample, endpoint=True)
    
    for i in xrange( len(t) ):
      y.append( random.gauss(self.m * t[i] + self.c, self.sig) )
    
    return t, y
  
  def Online(self, t):
    y = random.gauss(self.m * float(t) + self.c, self.sig) + self.disturbance.Online(t)

    return y

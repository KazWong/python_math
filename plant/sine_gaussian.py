import numpy as np
import random
import math
from disturbance import Disturbance

class SineGaussian(Disturbance):
  def __init__(self, _sigma, _A, _f, _p):
    super(SineGaussian, self).__init__()
  
    self.sig = float(_sigma)
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
    self.t = 0.
    
  def Model(self, t):
    return random.gauss(self.A*math.sin(2*math.pi*self.f*t+self.p), self.sig)
  
  def Reset(self, _m, _c):
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
    
  def Offline(self, end_t, sample_rate):
    t = []
    y = []
    
    sample = float(end_t) * sample_rate;
    t = np.linspace(0., end_t, sample, endpoint=True)
    
    for i in xrange( len(t) ):
      y.append( self.Model(t[i]) )
    
    return t, y
  
  def Online(self, t):
    y = self.Model(t) + self.disturbance.Online(t)

    return y

import numpy as np
import random

class LinearGaussian:
  def __init__(self, _resolution, _sigma, _m, _c):
    self.sig = float(_sigma)
    self.re = float(_resolution)
    self.m = float(_m)
    self.c = float(_c)
    self.y = []
    self.t = []
  
  def Offline(self, end_t):
    self.y = []
    self.t = []
    
    sample = float(end_t) * self.re;
    self.t = np.linspace(0., end_t, sample, endpoint=True)
    
    for i in xrange( len(self.t) ):
      self.y.append( random.gauss(self.m * self.t[i] + self.c, random.uniform(0., self.sig)) )
    
    return self.t, self.y
  
  def Reset(self):
    self.y = []
    self.t = [0.]
  
  def Read(self):
    self.t.append(self.t[-1] + 1./self.re)
    self.y.append( random.gauss(self.m * self.t[-1] + self.c, random.uniform(0., self.sig)) )
    
    return self.t[-1], self.y[-1]
  
  def Set(self, _m, _c):
    self.m = float(_m)
    self.c = float(_c)

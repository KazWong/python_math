import numpy as np
import random

class DryAirGaussian:
  def __init__(self, _resolution, _sigma, _length, _width, _height, _temperature):
    self.sig = float(_sigma)
    self.re = float(_resolution)
    self.l = float(_length)
    self.w = float(_width)
    self.h = float(_height)
    self.y = []
    self.t = []
    self._Q = 0
    self._T = _temperature
    
  def Model():
    density = 1.01325/( 287.058 * (273.16 + self._T) )
    volume = 
    self._T = self._T - Q/()
  
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

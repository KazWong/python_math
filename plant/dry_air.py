import numpy as np
import random

class DryAir:
  def __init__(self, _resolution, _volume, _temperature):
    self.re = float(_resolution)
    self._volume = float(_volume)
    self.y = []
    self.t = []
    self._init_T = float(_temperature)
    self._T = self._init_T
    self._Q = 1.01325/( 287.058 * (273.16 + self._T) ) * self._volume * 1005. * (273.16 + self._T)
    self._Q_new = self._Q
    self.noise = 0
    self.Reset()
    
  def Model(self):
    density = 1013.25/( 287.058 * (273.16 + self._T) )
    print density
    self._T = self._T - (self._Q_new - self._Q + self.noise)/(density * self._volume * 1005.)
    print self._T
    self._Q = self._Q_new
    
    return self._T
  
  def Offline(self, end_t):
    self.y = []
    self.t = []
    
    sample = float(end_t) * self.re;
    self.t = np.linspace(0., end_t, sample, endpoint=True)
    
    for i in xrange( len(self.t) ):
      self.y.append( self.Model() )
    
    return self.t, self.y
  
  def Reset(self):
    self.y = [self._init_T]
    self.t = [0.]
    self._T = self._init_T
  
  def Online(self, _Q):
    self._Q_new = ( float(_Q) / self.re ) + self._Q_new # per second change
    self.t.append(self.t[-1] + 1./self.re)
    self.y.append( self.Model() )
    
    return self.t[-1], self.y[-1]

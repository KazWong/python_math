import numpy as np
import random
from disturbance import Disturbance

class DryAir:
  def __init__(self, _sample_rate, _volume, _temperature, _disturbance = None):
    self.sample_rate = float(_sample_rate)
    self._volume = float(_volume)
    self.y = []
    self.t = []
    self._init_T = float(_temperature)
    self._T = self._init_T
    self._Q = 1.01325/( 287.058 * (273.16 + self._T) ) * self._volume * 1005. * (273.16 + self._T)
    self._Q_new = self._Q
    if (isinstance(_disturbance, Disturbance)):
      self.disturbance = _disturbance
    else:
      self.disturbance = Disturbance()
      
    self.Reset()
    
  def Model(self, t):
    density = 1013.25/( 287.058 * (273.16 + self._T) )
    energy_exchange = self._Q_new - self._Q + self.disturbance.Online(t)
    self._T = self._T + energy_exchange/(density * self._volume * 1005.)
    self._Q = self._Q_new
    
    return self._T
  
  def Reset(self):
    self.t = [0.]
    self.y = [self._init_T]
    self._T = self._init_T
  
  def Offline(self, end_t):
    self.y = []
    self.t = []
    
    sample = float(end_t) * self.sample_rate;
    self.t = np.linspace(0., end_t, sample, endpoint=True)
    
    for i in xrange( len(self.t) ):
      self.y.append( self.Model(self.t[i]) )
    
    return self.t, self.y

  def Online(self, _Q):
    self._Q_new = ( float(_Q) / self.sample_rate ) + self._Q_new # per second change
    self.t.append(self.t[-1] + 1./self.sample_rate)
    self.y.append( self.Model(self.t[-1]) )
    
    return self.t[-1], self.y[-1]

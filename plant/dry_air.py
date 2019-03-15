import numpy as np
import random
from disturbance import Disturbance

class DryAir:
  def __init__(self, _sample_rate, _input_delay, _volume, _temperature, _disturbance = None, _measure_noise = None):
    self.sample_rate = float(_sample_rate)
    self._volume = float(_volume)
    self.y = []
    self.t = []
    self.input_delay = _input_delay
    self._init_T = float(_temperature)
    self._T = self._init_T
    self._Q = self.Density(self._init_T) * self._volume * 1005. * (273.16 + self._T)
    self._Q_new = np.full( int(self.sample_rate * self.input_delay), self._Q )
    if (isinstance(_disturbance, Disturbance)):
      self.disturbance = _disturbance
    else:
      self.disturbance = Disturbance()
    
    if (isinstance(_measure_noise, Disturbance)):
      self.measure_noise = _measure_noise
    else:
      self.measure_noise = Disturbance()
      
    self.Reset()
    
  def Density(self, T):
    return 101325./( 287.058 * (273.16 + float(self._T)) )
    
  def Model(self, t):
    energy_exchange = self._Q_new[0] - self._Q + self.disturbance.Online(t)
    self._T = self._T + energy_exchange/(self.Density(self._T) * self._volume * 1005.)
    self._Q = self._Q_new[0]
    np.delete(self._Q_new, [0])
    
    T = self._T + self.measure_noise.Online(t)
    
    return T
  
  def Reset(self):
    self.t = [0.]
    self.y = [self._init_T]
    self._T = self._init_T
  
  def Offline(self, end_t):
    self.t = []
    self.y = []
    
    sample = float(end_t) * self.sample_rate
    self.t = np.linspace(0., end_t, sample, endpoint=True)
    
    for i in xrange( len(self.t) ):
      self.y.append( self.Model(self.t[i]) )
    
    return self.t, self.y

  def Online(self, _Q):
    self._Q_new = np.append( self._Q_new, float(_Q) + self._Q_new )
    self.t = np.append( self.t, self.t[-1] + 1./self.sample_rate )
    self.y = np.append( self.y, self.Model(self.y[-1]) )

    
    return self.t[-1], self.y[-1]

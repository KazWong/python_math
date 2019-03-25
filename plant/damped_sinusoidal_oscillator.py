import math
import numpy as np
import random
from .signal import Signal, Ideal

class DampedSinOsc:
  def __init__(self, _sample_rate, _damping_ratio, _ampitude, _angular_frequency, _phase_shift, _disturbance = None, _measure_noise = None):
    self.sample_rate = float(_sample_rate)
    self.t = []
    self.y = []
    self.dr = float(_damping_ratio)
    self.f = float(_angular_frequency)
    self.p = float(_phase_shift)
    self.a = float(_ampitude)
    
    if (isinstance(_disturbance, Signal)):
      self.disturbance = _disturbance
    else:
      self.disturbance = Ideal()
    
    if (isinstance(_measure_noise, Signal)):
      self.measure_noise = _measure_noise
    else:
      self.measure_noise = Ideal()
      
    self.Reset()
  
  def Reset(self):
    self.t = [0.]
    self.y = [self.a*math.sin(self.p)]  
    
  def Model(self, t):
    z = self.a*math.exp(-self.dr*2.*math.pi*self.f*t)*math.sin(math.sqrt(1.-self.dr**2.)*2.*math.pi*self.f*t+self.p)
    z = z + self.measure_noise.Online(t)
    
    return z

  def Offline(self, end_t):
    self.t = []
    self.y = []
    
    sample = float(end_t) * self.sample_rate
    self.t = np.linspace(0., end_t, sample, endpoint=True)
    
    for i in range( len(self.t) ):
      self.y.append( self.Model(self.t[i]) )
    
    return self.t, self.y

  def Online(self):
    self.t = np.append( self.t, self.t[-1] + 1./self.sample_rate )
    self.y = np.append( self.y, self.Model(self.y[-1]) )

    
    return self.t[-1], self.y[-1]

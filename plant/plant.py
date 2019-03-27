import numpy as np
from ..signal.signal import Signal, Ideal

class Plant(object):
  def __init__(self, _sample_rate, _di = None, _do = None):
    self.sample_rate = float(_sample_rate)
    self.sim_t = - 1./(self.sample_rate)
    self.t = np.array([])
    self.x = np.array([])

    if (isinstance(_di, Signal)):
      self.di = _di
    else:
      self.di = Ideal()
    
    if (isinstance(_do, Signal)):
      self.do = _do
    else:
      self.do = Ideal()

  def Reset(self):
    self.sim_t = - 1./(self.sample_rate)
    self.t = np.array([])
    self.x = np.array([])
    
  def Model(self, t):
    raise NotImplementedError()
  
  def Offline(self, end_t):
    sample = float(end_t) * (self.sample_rate) + 1
    self.t = np.linspace(0., end_t, sample, endpoint=True)
    self.x = np.array([self.Model(self.t[_]) for _ in range(int(sample))])
    return self.t, self.x

  def Online(self):
    self.sim_t = round(self.sim_t + 1./(self.sample_rate), 4)
    self.t = np.append( self.t, self.sim_t )
    self.x = np.append( self.x, self.Model(self.sim_t) )
    return self.t[-1], self.x[-1]

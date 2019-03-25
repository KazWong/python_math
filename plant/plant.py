import numpy as np
from .signal import Signal, Ideal

class Plant(object):
  def __init__(self, _sample_rate, _di = None, _do = None):
    self.sample_rate = float(_sample_rate)
    self.t = np.array([])
    self.y = np.array([])

    if (isinstance(_di, Signal)):
      self.di = _di
    else:
      self.di = Ideal()
    
    if (isinstance(_do, Signal)):
      self.do = _do
    else:
      self.do = Ideal()

  def Reset(self):
    self.t = np.array([])
    self.y = np.array([])
    
  def Model(self, t):
    raise NotImplementedError()
  
  def Offline(self, end_t):
    self.Reset()
    sample = float(end_t) * self.sample_rate
    self.t = np.linspace(0., end_t, sample, endpoint=True)
    y = np.array([self.Model(t[_]) for _ in range(int(sample))])
    for i in range( len(self.t) ):
      self.y.append( self.Model(self.t[i]) )
    
    return self.t, self.y

  def Online(self, _Q):
    self._Q_new = float(_Q) + self._Q_new[-1]
    self.t = np.append( self.t, self.t[-1] + 1./self.sample_rate )
    self.y = np.append( self.y, self.Model(self.y[-1]) )

    
    return self.t[-1], self.y[-1]

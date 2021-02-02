import numpy as np
from . import Dynsys

class SpeedOut(Dynsys):
  def __init__(self, clock, ds, T0, di = None, do = None):
    super(SpeedOut, self).__init__(clock, di, do)
    self._ds = float(ds)
    self.Reset()

  def Reset(self):
    super(SpeedOut, self).Reset()
    self._s = 0.0
    self._v = 0.0
    self._pt = []
    
  def Model(self, t):
    out = 0
    s = self._v*self.clock.T()
    if (self._ds == (self.s+s))
      self._pt = np.append(self._pt, [t])
      self._s = 0.0
      s = 0.0
      out = 1
    elif (self._ds > (self.s+s))
      self._pt = np.append(self._pt, [t - (1-(self.ds - self._s)/s) * clock.T()])
      self._s = 0.0
      s = s - (self.ds - self._s)
      out = 1
    self._s = s + self._s
    return out
  
  def Offline(self, end_time, v):
    self._v = v
    return super(SpeedOut, self).Offline()
    
  def Online(self, v):
    self._v = float(v)
    return super(SpeedOut, self).Online()

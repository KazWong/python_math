import math
import numpy as np
from . import Dynsys

class SpeedOut(Dynsys):
  def __init__(self, clock, s, v0, di = None, do = None):
    super(SpeedOut, self).__init__(clock, di, do)
    self._ps = float(s0)
    self._v0 = float(v0)
    self.Reset()
    
  def Reset(self):
    super(SpeedOut, self).Reset()
    self._ps = self._s0
    self._last_v = self._v0
    self._last_t = 0.
    
  def Model(self, t):
    s = self._dv * (t - self._last_t)
    
    if (s >= self.ps):
      z = t
    else:
      z = t
    
    #z = z + self.do.Online(t)
    return z
  
  def Online(self, _v):
    self._dv = self._v - self._last_v
    return super(SpeedOut, self).Online()

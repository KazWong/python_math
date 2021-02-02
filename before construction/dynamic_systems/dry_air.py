import numpy as np
from . import Dynsys

class DryAir(Dynsys):
  def __init__(self, clock, v, T0, di = None, do = None):
    super(DryAir, self).__init__(clock, di, do)
    self._v = float(v)
    self._T0 = float(T0)
    self.Reset()

  def Reset(self):
    super(DryAir, self).Reset()
    self._T = self._T0
    self._Q = self.Density(self._T0) * self._v * 1005. * (273.16 + self._T0)
    self._Q_new = self._Q
  
  def Density(self, T):
    return 101325./( 287.058 * (273.16 + float(self._T)) )
    
  def Model(self, t):
    energy_exchange = self._Q_new - self._Q + self.di.Online(t)
    self._T = self._T + energy_exchange/(self.Density(self._T) * self._v * 1005.)
    self._Q = self._Q_new
    T = self._T + self.do.Online(t)
    return T
  
  def Online(self, _Q=0.):
    self._Q_new = float(_Q) + self._Q_new
    return super(DryAir, self).Online()

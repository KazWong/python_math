import numpy as np
import random
from .plant import Plant

class Newtonian(Plant):
  def __init__(self, _sample_rate, _X0=[0.], _di = None, _do = None):
    super(Newtonian, self).__init__(_sample_rate, _di, _do, 4, 4)
    
    self.Valid(_X0)
    self._len = len(_X0)
    self._X0 = np.array( _X0 + [0.]*(4-len(_X0)) )
    self.Reset()

  def Reset(self):
    super(Newtonian, self).Reset()
    
    self._X = ( self._X0 / self.sample_rate )
    
  def Model(self, t):
    for i in range(4):
      self._X[i] += (self.di[i].Online(t) / self.sample_rate)
    x = self._X[0] + self._X[1]*t + 0.5*self._X[2]*t**2 + 0.16666*self._X[3]*t**3 + self.do[0].Online(t)
    v = self._X[1] + self._X[2]*t + 0.3333*self._X[3]*t**2 + self.do[1].Online(t)
    a = self._X[2] + 0.6666*self._X[3]*t + self.do[2].Online(t)
    j = 1.3333*self._X[3] + self.do[3].Online(t)
    
    return x, v, a, j
  
  def Online(self, _c1=[0.]):
    self.Valid(_c1)
    self._X += (np.array( _c1 + [0.]*(4-len(_c1)) ) / self.sample_rate)
    super(Newtonian, self).Online()
    return self.t[-1], self.x[-4:]
  
  def Valid(self, _l):
    if (isinstance(_l, list)):
      if (len(_l) > 4):
        raise LookupError()
    else:
      raise TypeError()

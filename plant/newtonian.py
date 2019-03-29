import numpy as np
import random
from . import Plant

class Newtonian(Plant):
  def __init__(self, clock, X0=[0.], di = None, do = None):
    super(Newtonian, self).__init__(clock, di, do, 4, 4)
    self.Valid(X0)
    self._len = len(X0)
    self._X0 = np.array( X0 + [0.]*(4-len(X0)) )
    self.Reset()

  def Reset(self):
    super(Newtonian, self).Reset()
    self._X = self._X0
    
  def Model(self, t):
    for i in range(4):
      self._X[i] += self.di[i].Online(t)
    x = self._X[0] + self._X[1]*t + 0.5*self._X[2]*t**2 + 0.16666*self._X[3]*t**3 + self.do[0].Online(t)
    v = self._X[1] + self._X[2]*t + 0.3333*self._X[3]*t**2 + self.do[1].Online(t)
    a = self._X[2] + 0.6666*self._X[3]*t + self.do[2].Online(t)
    j = 1.3333*self._X[3] + self.do[3].Online(t)
    return x, v, a, j
  
  def Online(self, _c1=[0.]):
    self.Valid(_c1)
    self._X += np.array( _c1 + [0.]*(4-len(_c1)) )
    super(Newtonian, self).Online()
    return self.x[-4:]
  
  def Valid(self, _l):
    if (isinstance(_l, list)):
      if (len(_l) > 4):
        raise LookupError()
    else:
      raise TypeError()

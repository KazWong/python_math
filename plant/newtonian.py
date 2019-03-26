import numpy as np
import random
from .plant import Plant

class Newtonian(Plant):
  def __init__(self, _sample_rate, _A0=[0.], _di = None, _do = None):
    super(Newtonian, self).__init__(_sample_rate, _di, _do)
    
    self.Valid(_A0)
    self._len = len(_A0)
    self._A0 = np.array( _A0 + [0.]*(4-len(_A0)) )
    self.Reset()

  def Reset(self):
    self.t = np.array([0.])
    self.x = np.array([self._A0])
    self._A = self._A0
    
  def Model(self, t):
    self._A[self._len-1] += (self.di.Online(t) / self.sample_rate)
    x = self._A[0] + self._A[1]*t + 0.5*self._A[2]*t**2 + 0.16666*self._A[3]*t**3
    v = self._A[1] + self._A[2]*t + 0.3333*self._A[3]*t**2
    a = self._A[2] + 0.6666*self._A[3]*t
    j = 1.3333*self._A[3]
    x += self.do.Online(t)
    return x, v, a, j
  
  def Online(self, _c1=[0.]):
    self.Valid(_c1)
    c1 = np.array( _c1 + [0.]*(4-len(_c1)) )
    self._A += c1
    return super(Newtonian, self).Online()
  
  def Valid(self, _l):
    if (isinstance(_l, list)):
      if (len(_l) > 4):
        raise LookupError()
    else:
      raise TypeError()

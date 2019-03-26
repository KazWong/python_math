import numpy as np
import random
from .plant import Plant

class Motion(Plant):
  def __init__(self, _sample_rate, _A0=[0.], _di = None, _do = None):
    super(Motion, self).__init__(_sample_rate, _di, _do)
    
    if (isinstance(_A0, list)):
      if (len(_A0) > 4):
        return LookupError()
    else:
      return TypeError()
        
    self._len = len(_A0)
    self._A0 = np.array( _A0 + [0.]*(4-len(_A0)) )
    self.Reset()

  def Reset(self):
    self.t = np.array([0.])
    self.x = self._A0[0]
    
  def Model(self, t):
    self.x = self._A0[0] + self._A0[1]*t + 0.5*self._A0[2]*t**2 + 0.16666*self._A0[3]*t**3
    x = self.x + self.do.Online(t)
    return x
  
  def Online(self, _A=[0.]):
    A = np.array( _A + [0.]*(4-len(_A)) )
    self._A += A
    super(Motion, self).Online()

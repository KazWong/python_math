import numpy as np
import random
import math
from . import Signal

class SineGaussian(Signal):
  def __init__(self, clock, sigma, A, f, p = 0.):
    super(SineGaussian, self).__init__(clock)
  
    self.sig = float(sigma)
    self.A = float(A)
    self.f = float(f)
    self.p = float(p)
      
  def Model(self, t):
    rand = self.sig * np.random.randn( len(t) )
    return rand + self.A*np.sin(2.*math.pi*self.f*t+self.p)

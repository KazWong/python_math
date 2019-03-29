import numpy as np
import random
from . import Signal

class LinearGaussian(Signal):
  def __init__(self, clock, sigma, m, c):
    super(LinearGaussian, self).__init__(clock)
    self.sig = float(sigma)
    self.m = float(m)
    self.c = float(c)
      
  def Model(self, t):
    rand = self.sig * np.random.randn( np.array(t).size )
    return rand + (self.m * t + self.c)

import numpy as np
import random
from .signal import Signal

class LinearGaussian(Signal):
  def __init__(self, _sigma, _m, _c):
    super(LinearGaussian, self).__init__()
  
    self.sig = float(_sigma)
    self.m = float(_m)
    self.c = float(_c)
  
  def Reset(self, _m, _c):
    self.m = float(_m)
    self.c = float(_c)
      
  def Model(self, t):
    return random.gauss(self.m * t + self.c, self.sig)

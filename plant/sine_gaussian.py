import numpy as np
import random
import math
from .signal import Signal

class SineGaussian(Signal):
  def __init__(self, _sigma, _A, _f, _p = 0.):
    super(SineGaussian, self).__init__()
  
    self.sig = float(_sigma)
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
    self.t = 0.
  
  def Reset(self, _m, _c):
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
      
  def Model(self, t):
    return random.gauss(self.A*math.sin(2*math.pi*self.f*t+self.p), self.sig)

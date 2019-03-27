import numpy as np
import random
import math
from .signal import Signal
from .sine_gaussian import SineGaussian

class Square(Signal):
  def __init__(self, _sigma, _A, _f, _p = 0.):
    super(Square, self).__init__()
  
    self.sig = float(_sigma)
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
    
    sine3 = SineGaussian(0., 2.7, 6.4, 0.)
    sine3 = SineGaussian(0., 2.7, 6.4, 0.)
    sine3 = SineGaussian(0., 2.7, 6.4, 0.)
    sine2 = SineGaussian(0., 1.7, 12.3, 0.)
    sine1 = SineGaussian(0., 15.7, 3.3, 0.)
    
    sine
  
  def Reset(self, _m, _c):
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
      
  def Model(self, t):
    return random.gauss(self.A*math.sin(2*math.pi*self.f*t+self.p), self.sig)

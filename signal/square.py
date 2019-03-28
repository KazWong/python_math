import numpy as np
import math
from .signal import Signal
from .sine_gaussian import SineGaussian
from .linear_gaussian import LinearGaussian

class Square(Signal):
  def __init__(self, _sigma, _terms, _A, _f, _p = 0.):
    super(Square, self).__init__()
  
    self.terms = int(_terms)
    self.sig = float(_sigma)
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
    
    g = 4./math.pi
    sine = []
    for i in range(1, self.terms+1):
      h = 2*i-1
      sine.append( SineGaussian(self.sig, g*self.A/h, h*self.f, self.p) )
      if (i>1):
        sine[i-2].Cascade(sine[i-1])

    self.sine = LinearGaussian(0., 0., self.A)
    self.sine.Cascade(sine[0])
    
  
  def Reset(self, _m, _c):
    self.A = float(_A)
    self.f = float(_f)
    self.p = float(_p)
      
  def Model(self, t):
    return self.sine.Online(t)

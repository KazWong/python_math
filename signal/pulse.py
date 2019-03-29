import numpy as np
import math
from . import Signal
from .sine_gaussian import SineGaussian
from .linear_gaussian import LinearGaussian

###
class Impulse(Signal):
  def __init__(self, clock, t, A):
    super(Impulse, self).__init__(clock)
    self.t = t
    self.A = A
    self.last_t = 0.
    
  def Model(self, t):
    y = 0.
    if (t == self.t or (t > self.t and self.last_t < self.t) ):
      y = self.A
    self.last_t = t
    
    return y


###
class Square(Signal):
  def __init__(self, clock, sigma, terms, A, f):
    super(Square, self).__init__(clock)
  
    self.terms = int(terms)
    self.sig = float(sigma)
    self.A = float(A/2.)
    self.f = float(f)
    self.p = 0.
    
    g = 4./math.pi
    sine = []
    for i in range(1, self.terms+1):
      h = 2*i-1
      sine.append( SineGaussian(clock, self.sig, g*self.A/h, h*self.f, self.p) )
      if (i>1):
        sine[i-2].Cascade(sine[i-1])

    self.sine = LinearGaussian(clock, 0., 0., self.A)
    self.sine.Cascade(sine[0])
    
  def Model(self, t):
    return self.sine.Online(t)


###
class PWM(Signal):
  def __init__(self, clock, max_A, min_A, f, D=0.5, shift=0.0):
    super(PWM, self).__init__(clock)
  
    self.max = float(max_A)
    self.min = float(min_A)
    self.T = float(1./f)
    self.D = float(D*self.T)
    self.shift = float(shift)
      
  def Model(self, t):
    if ( (t+self.shift)%self.T > self.D ):
      return self.max
    else:
      return self.min

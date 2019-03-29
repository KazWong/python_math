import numpy as np
import math
from . import Signal
from .sine_gaussian import SineGaussian
from .linear_gaussian import LinearGaussian


###
class Square(Signal):
  def __init__(self, clock, sigma, terms, A, f, shift = 0.0):
    super(Square, self).__init__(clock)
    self.terms = int(terms)
    self.sig = float(sigma)
    self.A = float(A/2.)
    self.f = float(f)
    self.shift = float(shift*f)
    
    g = 4./math.pi
    sine = []
    for i in range(1, self.terms+1):
      h = 2*i-1
      sine.append( SineGaussian(clock, 0.0, g*self.A/h, h*self.f) )
      if (i>1):
        sine[i-2].Cascade(sine[i-1])

    self.sine = LinearGaussian(clock, sigma, 0., self.A)
    self.sine.Cascade(sine[0])
    
  def Model(self, t):
    return self.sine.Online(t - self.shift)


###
class PWM(Signal):
  def __init__(self, clock, sigma, terms, A, f, d, shift=0.0):
    super(PWM, self).__init__(clock)
    self.terms = int(terms)
    self.sig = float(sigma)
    self.A = float(A)
    self.f = float(f)
    self.d = float(d)
    self.shift = float(f*shift)
      
  def Model(self, t):
    sine = np.array([0.]*len(t))
    pi = math.pi
    for i in range(1, self.terms+1):
      sine += (1./i)*np.sin(pi*i*self.d)*np.cos(2*pi*i*self.f*(t - self.shift))
    rand = self.sig * np.random.randn( len(sine) )
    sine = rand + self.A*( (sine * 2/pi) + self.d )
    return sine
    
    

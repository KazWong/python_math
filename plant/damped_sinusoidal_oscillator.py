import math
import numpy as np
from . import Plant

class DampedSinOsc(Plant):
  def __init__(self, clock, damping_ratio, A, angular_frequency, phase_shift, di = None, do = None):
    super(DampedSinOsc, self).__init__(clock, di, do)
    self._dr = float(damping_ratio)
    self._omega = 2.*math.pi*float(angular_frequency)
    self._p = float(phase_shift)
    self._A = float(A)
    self._g = math.sqrt(1.-self._dr**2.)
    self.Reset()
    
  def Model(self, t):
    z = self._A*math.exp(-self._dr*self._omega*t)*math.sin(self._g*self._omega*t+self._p)
    z = z + self.do.Online(t)
    return z

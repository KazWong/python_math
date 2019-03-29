import math
import numpy as np
from . import Plant

class DampedSinOsc(Plant):
  def __init__(self, _sample_rate, _damping_ratio, _A, _angular_frequency, _phase_shift, _di = None, _do = None):
    super(DampedSinOsc, self).__init__(_sample_rate, _di, _do)
    
    self._dr = float(_damping_ratio)
    self._omega = 2.*math.pi*float(_angular_frequency)
    self._p = float(_phase_shift)
    self._A = float(_A)
    self._g = math.sqrt(1.-self._dr**2.)
    self.Reset()
    
  def Model(self, t):
    z = self._A*math.exp(-self._dr*self._omega*t)*math.sin(self._g*self._omega*t+self._p)
    z = z + self.do.Online(t)
    return z

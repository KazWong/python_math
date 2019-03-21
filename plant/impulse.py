import numpy as np
import random
from .signal import Signal

class Impulse(Signal):
  def __init__(self, _t, _A):
    super(Impulse, self).__init__()
  
    self.A = float(_A)
    self.t = float(_t)
  
  def Model(self, t):
    y = 0.
    if (t == self.t)
      y = self.A
    return y
      
  def Reset(self, _t, _A):
    self.A = float(_A)
    self.t = float(_t)

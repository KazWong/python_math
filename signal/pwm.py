import numpy as np
import random
import math
from .signal import Signal

class PWM(Signal):
  def __init__(self, _max, _min, _T, _D=0.5):
    super(PWM, self).__init__()
  
    self.max = float(_max)
    self.min = float(_min)
    self.T = float(_T)
    self.D = float(_D)
  
  def Reset(self, _max, _min, _T, _D):
    self.max = float(_max)
    self.min = float(_min)
    self.T = float(_T)
    self.D = float(_D)
      
  def Model(self, t):
    if (t%self.T > self.D):
      return self.max
    else:
      return self.min 

import numpy as np
import random
from disturbance import Disturbance

class Impulse(Disturbance):
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
    
  def Offline(self, end_t, sample_rate):
    t = []
    y = []
    
    sample = float(end_t) * sample_rate;
    t = np.linspace(0., end_t, sample, endpoint=True)
    y.append( self.Model(t) )
      
    return t, y
  
  def Online(self, t):
    y = self.Model(self, t) + self.disturbance.Online(t)

    return y

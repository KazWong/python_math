import numpy as np

class Disturbance(object):
  def __init__(self):
    self.disturbance = Ideal()
    
    self.t = 0.
  
  def Reset(self):
    self.t = 0.
  
  def Offline(self, end_t, sample_rate):
    t = []
    y = []
    
    sample = float(end_t) * sample_rate
    t = np.linspace(0., end_t, sample, endpoint=True)
    y = [0.] * len(t)
    
    return t, y
    
  def Online(self, t):   
    return 0.
  
  def Cascade(self, _disturbance):
    if (isinstance(_disturbance, Disturbance)):
      self.disturbance = _disturbance

class Ideal(Disturbance):
  def __init__(self):
    self.disturbance = None
    return
    
  def Online(self, t):
    return 0.
  
  def Cascade(self, _disturbance):
    self.disturbance = None

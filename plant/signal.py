import numpy as np

class Signal(object):
  def __init__(self):
    self.signal = Ideal()
  
  def Reset(self):
    raise NotImplementedError()
  
  def Model(self, t):
    raise NotImplementedError()
  
  def Offline(self, end_t, sample_rate):
    sample = float(end_t) * sample_rate;
    t = np.linspace(0., end_t, sample, endpoint=True)
    y = np.array([self.Model(t[_]) for _ in range(int(sample))])
    
    t1, y1 = self.signal.Offline(end_t, sample_rate)
    
    return t, y+y1
    
  def Online(self, t):   
    return self.Model(t) + self.signal.Online(t)
  
  def Cascade(self, _signal):
    if (isinstance(_signal, Signal)):
      self.signal = _signal

class Ideal(Signal):
  def __init__(self):
    self.signal = None
    return
    
  def Reset(self):
    pass
  
  def Model(self, t):
    pass
  
  def Offline(self, end_t, sample_rate):
    sample = float(end_t) * sample_rate;
    t = np.linspace(0., end_t, sample, endpoint=True)
    y = np.array([0.] * int(sample))
    
    return t, y
    
  def Online(self, t):   
    return self.Model(t)
  
  def Cascade(self, _signal):
    self.signal = None

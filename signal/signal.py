import numpy as np

class Signal(object):
  def __init__(self):
    self.signal = Ideal()
  
  def Reset(self):
    raise NotImplementedError()
  
  def Model(self, t):
    raise NotImplementedError()
  
  def Offline(self, _t, sample_rate=None):
    if (sample_rate is not None):
      t = np.linspace(0., _t, int(_t*sample_rate+1), endpoint=True)
    else:
      t = _t

    y = np.array([self.Model(t[_]) for _ in range(len(t))])
    t, y1 = self.signal.Offline(t)
    
    return t, y + y1
    
  def Online(self, t):   
    return self.Model(t) + self.signal.Online(t)
  
  def Cascade(self, _signal):
    if (isinstance(_signal, Signal)):
      self.signal = _signal

class Ideal(Signal):
  def __init__(self):
    self.signal = None
    
  def Reset(self):
    pass
  
  def Model(self, t):
    pass
  
  def Offline(self, t):
    y = np.array([0.] * len(t))
    return t, y
    
  def Online(self, t):   
    return 0.
  
  def Cascade(self, _signal):
    self.signal = None

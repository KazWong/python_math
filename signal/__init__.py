import numpy as np

###
class Signal(object):
  def __init__(self, clock):
    self.signal = Ideal()
    self.clock = clock
  
  def Model(self, t):
    raise NotImplementedError()
  
  def Offline(self):
    y = np.array(self.Model(self.clock.timespace))
    y1 = self.signal.Offline()
    return y + y1
    
  def Online(self, t = None):
    if (t is None) :  
      return self.Model(self.clock.t) + self.signal.Online()
    else:
      return self.Model(t) + self.signal.Online(t)
  
  def Cascade(self, signal):
    if (isinstance(signal, Signal)):
      self.signal = signal


###
class Ideal(Signal):
  def __init__(self):
    self.signal = None
    
  def Model(self, t):
    pass
  
  def Offline(self):
    return 0.
    
  def Online(self, t):   
    return 0.
  
  def Cascade(self, signal):
    self.signal = None
    
    
###
class Time:
  def __init__(self, sampling_rate):
    self._sampling_rate = float(sampling_rate)
    self.Reset()
    
  def Reset(self):
    self.step = (1./self._sampling_rate)%1 * 1e9
    self.s = 0
    self.ns = 0
    self.timespace = np.array([0.])
  
  def Offline(self, end_time):
    self.Reset()
    self.timespace = np.around(np.linspace(0., end_time, int(self._sampling_rate*end_time)+1), 10)
    self.s = int(self.timespace[-1])
    self.ns = int(self.timespace[-1]%1 * 1e9)
    
  def Tick(self):
    self.ns += self.step
    if (self.ns > 1e9):
      self.s += 1
      self.ns -= 1e9
    self.timespace = np.append(self.timespace, float(self.s) + float( np.round(self.ns / 1e9, 10) ) )
  
  def t(self):
    return self.timespace[-1]
    
  def Hz(self):
    return self._sampling_rate
  
  def T(self):
    return 1./self._sampling_rate
    
  def Len(self):
    return len(self.timespace)
    
  def Range(self):
    return range(len(self.timespace))
  

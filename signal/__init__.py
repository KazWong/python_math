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
  def __init__(self, sampling_rate, end_time = 1.):
    self._sampling_rate = float(sampling_rate)
    self._end_time = float(end_time)
    self.Reset()
    
  def Reset(self):
    self.t = 0.
    self.count = 0
    self.timespace = np.around(np.append(np.arange(0., self._end_time, 1./self._sampling_rate), self._end_time), 10)
    self.len = len(self.timespace)
    self.range = range(self.len)
    
  def Tick(self):
    if (self.count >= self.len):
      self.timespace = np.append( self.timespace[:-1], np.around(np.arange(self.timespace[-1], self.timespace[-1]+1.1*self.T(), self.T()), 10) )
      self.len += 1
      self.range = range(self.len)
    self.t = self.timespace[self.count]
    self.count += 1
    return self.t
  
  def Hz(self):
    return self._sampling_rate
  
  def T(self):
    return 1./self._sampling_rate
  
  

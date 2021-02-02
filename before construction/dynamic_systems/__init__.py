import numpy as np
from ..signal import Signal, Ideal, Time

class Dynsys(object):
  def __init__(self, clock, di = None, do = None, di_size = None, do_size = None):
    self.clock = clock
    self.x = np.array([])

    if (di_size is None):
      if (isinstance(di, Signal)):
        self.di = di
      else:
        self.di = Ideal()
    else:
      for i in range(di_size):
        if (not isinstance(di[i], Signal)):
          self.di = [Ideal()] * _di_size
        else:
          self.di = di

    if (do_size is None):
      if (isinstance(do, Signal)):
        self.do = do
      else:
        self.do = Ideal()
    else:
      for i in range(do_size):
        if (not isinstance(do[i], Signal)):
          self.do = [Ideal()] * do_size
        else:
          self.do = do

  def Reset(self):
    self.x = np.array([])
    
  def Model(self, t):
    raise NotImplementedError()
  
  def Offline(self, end_time):
    self.clock.Offline(end_time)
    ran = self.clock.Range()
    self.x = np.array([self.Model(self.clock.timespace[_]) for _ in ran])
    return self.x

  def Online(self):
    self.x = np.append( self.x, self.Model(self.clock.t) )
    return self.x[-1]

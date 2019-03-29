import numpy as np
from ..signal import Signal, Ideal, Time

class Plant(object):
  def __init__(self, clock, sample_rate, di = None, do = None, di_size = None, do_size = None):
    self.sample_rate = float(sample_rate)
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
    clock.Offline(end_time)
    self.x = np.array([self.Model(self.t[_]) for _ in clock.Range()])
    return self.x

  def Online(self):
    self.sim_t = round(self.sim_t + 1./(self.sample_rate), 4)
    self.t = np.append( self.t, self.sim_t )
    self.x = np.append( self.x, self.Model(self.sim_t) )
    return self.t[-1], self.x[-1]

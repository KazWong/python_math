import numpy as np
import math
from ..simtools import *

#Oriental Motor feedback signal
#Only simulate the trigger
#_t is pulse trigger time
#trigger_t is sampling time

class SpeedOut(Block):
    def __init__(self, wheel_r, gear_ratio):
        super(SpeedOut, self).__init__()
        self._spc = (math.pi*wheel_r)/(30*gear_ratio)
        self.Reset()

    def Reset(self):
        super(SpeedOut, self).Reset()
        self._u = np.array([])
        self._y = np.array([])
        self._dura = 0.0

    def Model(self):
        if (len(self._u) < 2):
            return 0

        ds = self._u[-1] - self._u[-2]
        if ((self._dura + ds) == self._spc):
            self._t = np.append(self._t, self._time.now())
            self._dura = 0.0
            return 1
        elif ((self._dura + ds) > self._spc):
            self._t = np.append(self._t, [self._time.timespace[-2] + (self._spc - self._dura)/ds * self._time.step])
            self._dura = (ds + self._dura) - self._spc
            return 1
        else:
            self._dura += ds
            return 0

    def Update(self, u):
        self._u = np.append(self._u, u)
        self._y = np.append(self._y, self.Model())
        return self._y[-1]

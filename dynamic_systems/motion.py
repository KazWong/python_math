import numpy as np
import random
from ..simtools import *

class Translation1D(Block):
    def __init__(self, x0=[0., 0., 0., 0.]):
        super(Translation1D, self).__init__()
        self._x0 = np.array(x0)
        self.Reset()

    def Reset(self):
        super(Translation1D, self).Reset()
        self._x = np.array([self._x0])
        self._u = np.empty((0, 3))
        self._y = np.empty((0, 4))

    def Model(self):
        #u = [v, a, j]
        dt = 0.0
        x = np.array(self._x[-1])
        if (len(self._t) >= 2):
            dt = self._t[-1] - self._t[-2]

            x[0] = self._x[-1][0] + (self._x[-1][1] + self._x[-2][1])*dt/2. + (self._u[-1][0] + self._u[-2][0])*dt/2. #pos
            x[1] = self._x[-1][1] + (self._x[-1][2] + self._x[-2][2])*dt/2. + (self._u[-1][1] + self._u[-2][1])*dt/2. #vel
            x[2] = self._x[-1][2] + (self._x[-1][3] + self._x[-2][3])*dt/2. + (self._u[-1][2] + self._u[-2][2])*dt/2. #acc
            x[3] = self._x[-1][3] + self._u[-1][2] #jerk
        self._x = np.append(self._x, np.array([x]), axis=0)
        return np.array([x])

    def Update(self, u):
        super(Translation1D, self).Update_t()
        self._u = np.append(self._u, u, axis=0)
        self._y = np.append(self._y, self.Model(), axis=0)
        return self._y[-1]

    def x(self):
        return self._x[-1]


class Rotation1D(Block):
    def __init__(self, x0=[0., 0., 0., 0.]):
        super(Rotation1D, self).__init__()
        self._x0 = np.array(x0)
        self.Reset()

    def Reset(self):
        super(Rotation1D, self).Reset()
        self._x = np.array([self._x0])
        self._u = np.empty((0, 3))
        self._y = np.empty((0, 4))

    def Model(self):
        #u = [theta, omega, alpha]
        dt = 0.0
        x = np.array(self._x[-1])
        if (len(self._t) >= 2):
            dt = self._t[-1] - self._t[-2]

            x[0] = self._x[-1][0] + (self._x[-1][1] + self._x[-2][1])*dt/2. + (self._u[-1][0] + self._u[-2][0])*dt/2. #theta
            x[1] = self._x[-1][1] + (self._x[-1][2] + self._x[-2][2])*dt/2. + (self._u[-1][1] + self._u[-2][1])*dt/2. #omega
            x[2] = self._x[-1][2] + (self._x[-1][3] + self._x[-2][3])*dt/2. + (self._u[-1][2] + self._u[-2][2])*dt/2. #alpha

            if (x[0] > 2.*math.pi):
                x[0] = x[0] - 2.*math.pi
        self._x = np.append(self._x, np.array([x]), axis=0)
        return np.array([x])

    def Update(self, u):
        super(Rotation1D, self).Update_t()
        self._u = np.append(self._u, u, axis=0)
        self._y = np.append(self._y, self.Model(), axis=0)
        return self._y[-1]

    def x(self):
        return self._x[-1]

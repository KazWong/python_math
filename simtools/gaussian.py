import numpy as np
import math
import random
from . import Block

class Gaussian(Block):
    def __init__(self, sigma):
        super(Gaussian, self).__init__()
        self.sig = float(sigma)
        self.Reset()

    def Reset(self):
        super(Gaussian, self).Reset()
        self._u = np.array([])
        self._y = np.array([])

    def Model(self):
        rand = self.sig * np.random.randn( 1 )
        return rand + self._u[-1]

class LinearGaussian(Block):
    def __init__(self, sigma, m, c):
        super(LinearGaussian, self).__init__()
        self.sig = float(sigma)
        self.m = float(m)
        self.c = float(c)
        self.Reset()

    def Reset(self):
        super(LinearGaussian, self).Reset()
        self._u = np.array([])
        self._y = np.array([])

    def Model(self):
        rand = self.sig * np.random.randn( 1 )
        return rand + (self.m*self._t[-1] + self.c)

class SineGaussian(Block):
    def __init__(self, sigma, A, f, p = 0.):
        super(SineGaussian, self).__init__()
        self.sig = float(sigma)
        self.A = float(A)
        self.f = float(f)
        self.p = float(p)
        self.Reset()

    def Reset(self):
        super(SineGaussian, self).Reset()
        self._u = np.array([])
        self._y = np.array([])

    def Model(self):
        rand = self.sig * np.random.randn( 1 )
        return rand + self.A*np.sin(2.*math.pi*self.f*self._t[-1]+self.p)

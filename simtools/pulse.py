import numpy as np
import math
from . import Block
from .gaussian import SineGaussian, LinearGaussian


###
class Square(Block):
    def __init__(self, sigma, terms, A, f, d, shift=0.0):
        super(Square, self).__init__()
        self.terms = int(terms)
        self.sig = float(sigma)
        self.A = float(A)
        self.f = float(f)
        self.d = float(d)
        self.shift = float(f*shift)
        self.Reset()

    def Reset(self):
        super(Square, self).Reset()
        self._u = np.array([])
        self._y = np.array([])

    def Model(self):
        sine = np.array([0.0])
        for i in range(1, self.terms+1):
            sine += (1./i)*np.sin(math.pi*i*self.d)*np.cos(2*math.pi*i*self.f*(self._t[-1] - self.shift))
        rand = self.sig * np.random.randn( 1 )
        sine = rand + self.A*( (sine * 2./math.pi) + self.d )
        return sine

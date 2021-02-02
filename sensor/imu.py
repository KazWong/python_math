import matplotlib.pyplot as plt
import numpy as np
import random
from ..simtools import *

# Reference
# IMU model: Oliver J. Woodman, "An introduction to inertial navigation" https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-696.pdf

class Accelometer1D(Block):
    def __init__(self, Hz, bias=0.0, sigma=0.0, bias_stability=0.0):
        super(Accelometer1D, self).__init__()
        self._hz = Hz
        self._b = bias
        self._sig = sigma
        self._bs = bias_stability
        self.Reset()

    def Reset(self):
        super(Accelometer1D, self).Reset()
        super(Accelometer1D, self).SetHz(self._hz)
        self._u = np.array([])
        self._y = np.array([])

    def Model(self):
        rand = self._sig * np.random.randn( 1 )
        return self._u[-1] + self._b + rand

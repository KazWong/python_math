import numpy as np
import random
from ..simtools import *

# Reference
# IMU model: Oliver J. Woodman, "An introduction to inertial navigation" https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-696.pdf
# Oliver J. Woodman, "Pedestrian localisation for indoor environments" https://www.cl.cam.ac.uk/research/dtg/www/files/publications/public/abr28/ojw28_thesis.pdf

class Accelometer1D(Block):
    # input acceleration, output the value with imu noise
    # Additive noise: bias error, white noise, bias instability
    # s = perfect sample, e = total additive error. IMU data = s + e
    # e = bias error + white noise + Bias instability
    def __init__(self, Hz, bias=0.0, sigma=0.0, random_walk =0.0):
        super(Accelometer1D, self).__init__()
        self._hz = Hz
        self._b = bias
        self._sig = sigma
        self._rw = random_walk
        self.Reset()

    def Reset(self):
        super(Accelometer1D, self).Reset()
        super(Accelometer1D, self).SetHz(self._hz)
        self._u = np.array([])
        self._y = np.array([])
        self._bs = 0.0

    def Model(self):
        rand = self._sig * np.random.randn( 1 )
        self._bs += self._rw * np.random.randn( 1 )
        return self._u[-1] + self._b + rand + self._bs

class Gyro1D(Block):
    # input omega
    def __init__(self, Hz, bias=0.0, sigma=0.0, random_walk=0.0):
        super(Gyro1D, self).__init__()
        self._hz = Hz
        self._b = bias
        self._sig = sigma
        self._rw = random_walk
        self.Reset()

    def Reset(self):
        super(Gyro1D, self).Reset()
        super(Gyro1D, self).SetHz(self._hz)
        self._u = np.array([])
        self._y = np.array([])
        self._bs = 0.0

    def Model(self):
        rand = self._sig * np.random.randn( 1 )
        self._bs += self._rw * np.random.randn( 1 )
        return self._u[-1] + self._b + rand + self._bs

import matplotlib.pyplot as plt
import numpy as np
from ..simtools import *

class Motion_vaj(Block):
    def __init__(self, T, x0=[0., 0., 0.], xn=[0., 0., 0.]):
        #xo = [v, a, j]
        #xn = [v, a, j]
        super(Motion_vaj, self).__init__()
        self._x0 = x0
        self._xn = xn
        self.T = T
        self._t_shift = 0.0
        T2 = T*T;T3 = T2*T;T4 = T3*T;T5 = T4*T
        self._A = np.array([[1, 0,   0,    0,     0,     0],
                            [0, 1,   0,    0,     0,     0],
                            [0, 0,   1,    0,     0,     0],
                            [1, T,  T2,   T3,    T4,    T5],
                            [0, 1, 2*T, 3*T2,  4*T3,  5*T4],
                            [0, 0,   2,  6*T, 12*T2, 20*T3]])
        self._B = np.array([x0[0], x0[1], x0[2], xn[0], xn[1], xn[2]])
        self._B.reshape([-1, 1])
        self._a = np.linalg.inv(self._A).dot(self._B)
        self.Reset()

    def Reset(self):
        super(Motion_vaj, self).Reset()
        self._x = np.array([self._x0])
        self._pos = np.array([])
        self._y = np.empty((0, 3))

    def Model(self):
        #u = [v, a, j]
        t1 = self._t[-1] + self._t_shift
        a = self._a

        x = np.array([[0., 0., 0.]])
        t2 = t1*t1;t3 = t2*t1;t4 = t3*t1;t5 = t4*t1;t6 = t5*t1

        pos = 0 + a[0]*t1 + a[1]*t2/2. + a[2]*t3/3. + a[3]*t4/4. + a[4]*t5/5. + a[5]*t6/6.
        x[0][0] = a[0] + a[1]*t1 + a[2]*t2 + a[3]*t3 + a[4]*t4 + a[5]*t5
        x[0][1] = a[1] + 2.*a[2]*t1 + 3.*a[3]*t2 + 4.*a[4]*t3 + 5.*a[5]*t4
        x[0][2] = 2.*a[2] + 6.*a[3]*t1 + 12.*a[4]*t2 + 20.*a[5]*t3
        self._x = np.append(self._x, x, axis=0)
        self._pos = np.append(self._pos, pos)
        return x

    def Update(self):
        super(Motion_vaj, self).Update_t()
        self._y = np.append(self._y, self.Model(), axis=0)
        return self._y[-1]

    def t_shift(self, t_shift=0.0):
        self._t_shift = t_shift

    def A(self):
        return self._a

    def Pos(self):
        return self._pos

import numpy as np
import math


class t:
    #class for share time, update in Time class
    step = 0.0
    timespace = []

    def now(self):
        if (self.timespace):
            return self.timespace[-1]
        else:
            return None


###
class Block(object):
    def __init__(self):
        self._time = t()
        self._t = np.array([])
        self._u = None
        self._y = None

    def Reset(self):
        self._k = -1
        self._f = None
        self._T = self._time.step
        self._t = np.array([])

    def SetHz(self, Hz):
        self._f = Hz
        self._T = None

    def SetT(self, T):
        self._T = T
        self._f = None

    def Model(self):
        raise NotImplementedError()

    def Update_t(self):
        #save u, y, kT
        if (self._time.now() is None):
            return None

        if (self._T == t.step):
            n = int(self._time.now()/self._T)
            self._t = np.append(self._t, self._time.now())
            self._k = n
            return True
        elif (self._T is not None):
            n = int(math.floor(self._time.now()/self._T))
            if (n > self._k):
                self._t = np.append(self._t, float(n)*self._T)
                self._k = n
                return True
        elif (self._f is not None):
            n = int(math.floor(self._time.now()*self._f))
            if (n > self._k):
                self._t = np.append(self._t, float(n)/self._f)
                self._k = n
                return True
        else:
            raise IOError()
        return False

    def Update(self, u):
        if (self.Update_t()):
            self._u = np.append(self._u, u)
            self._y = np.append(self._y, self.Model())
        return self._y[-1]

    def Y(self):
        return self._y
    def U(self):
        return self._u
    def timespace(self):
        return self._t
    def y(self):
        return self._y[-1]
    def u(self):
        return self._u[-1]
    def t(self):
        return self._t[-1]


###
class Time:
    # Simulation Time
    # step: floating point in sec

    def __init__(self, step, end_time = None):
        self._s_step = 0
        self._ns_step = 0
        self.count = 0
        self.time = t()
        if (end_time is not None):
            self._end_time = float(end_time)
        self.SetTick(step)
        self.Reset()

    def Reset(self):
        self._s = 0
        self._ns = 0
        self.count = 0
        self.time.timespace.clear()

    def SetTick(self, step = None):
        if (step is not None):
            self._step = float(step)
        t.step = self._step
        self._s_step = np.round(self._step)
        self._ns_step = (self._step - self._s_step)*1e9

    def Offline(self, end_time = None):
        # end_time: floating point of end time in sec, -1 is infinity for Online tick, Offline return error
        if (end_time is not None):
            self._end_time = float(end_time)
        if (self._end_time < 0.0 or self._end_time is None or (self._s_step == 0 and self._ns_step == 0)):
            raise RuntimeError('Offline mode end time < 0.0')
        self.Reset()
        [self.Tick() for _ in range( int(math.ceil(self._end_time/self._step))+1 )]
        return np.array(self.time.timespace)

    def Tick(self):
        if (not self.time.timespace):
            self.time.timespace.append(0.0)
        else:
            self.count += 1
            self._s += self._s_step
            self._ns += self._ns_step
            if (self._ns > 1e9):
                self._s += 1
                self._ns -= 1e9
            self.time.timespace.append( np.round( self._s + self._ns / 1e9, 9) )

    def T(self):
        return self._step

    def Len(self):
        return len(self.time.timespace)

    def now(self):
        if (self.time.now() is None):
            return 0.0
        return self.time.now()

    def timespace(self):
        return self.time.timespace

import numpy as np
import math
from enum import Enum


class t:
    #class for share time, update in Time class
    step = 0.0
    timespace = []

    def now(self):
        if (self.timespace):
            return self.timespace[-1]
        else:
            return None

class a6(Enum):
    x  = 0
    y  = 1
    z  = 2
    rx = 3
    ry = 4
    rz = 5


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
# quaternion:
#Yan-Bin Jia, "Quaternions and Rotations" https://www.weizmann.ac.il/sci-tea/benari/sites/sci-tea.benari/files/uploads/softwareAndLearningMaterials/quaternion-tutorial-2-0-1.pdf
#Moti Ben-Ari, "A Tutorial on Euler Angles and Quaternions" http://graphics.stanford.edu/courses/cs348a-17-winter/Papers/quaternion.pdf
#K.Groÿekatthöfer, Z.Yoon, "Intro ductionintoquaternionsforspacecraftattituderepresentation" http://www.tu-berlin.de/fileadmin/fg169/miscellaneous/Quaternions.pdf
class TF(object):
    # Z-Y-X
    def Euler2Quat(orien):
        Qx = np.array([math.cos(orien[2]/2.), math.sin(orien[2]/2.), 0.0, 0.0])
        Qy = np.array([math.cos(orien[1]/2.), 0.0, math.sin(orien[1]/2.), 0.0])
        Qz = np.array([math.cos(orien[0]/2.), 0.0, 0.0, math.sin(orien[0]/2.)])
        Q  = np.array(Qz.dot(Qy)).dot(Qx)
        return Q

    def RoMat2Quat(m):
        q0 = math.sqrt((m[0][0] + m[1][1] + m[2][2] + 1.)/2.)
        tmp = 4.*q0
        q1 = (m[2][1] - m[1][2])/tmp
        q2 = (m[0][2] - m[2][0])/tmp
        q3 = (m[1][0] - m[0][1])/tmp
        return np.array([q0, q1, q2, q3])

    def RoMat2Euler(m):
        r =  math.atan2(m[2][1], m[2][2])
        p = -math.asin(m[2][0])
        y =  math.atan2(m[1][0], m[0][0])
        return np.array([r, p, y])

    def Quat2RoMat(quat):
        #homogeneous expression
        q = quat
        Ro = np.array([ [q[0]**2 + q[1]**2 - 0.5, q[1]*q[2] - q[0]*q[3], q[0]*q[2] - q[1]*q[3] ],
                        [q[0]*q[3] - q[1]*q[2], q[0]**2 + q[2]**2 - 0.5, q[2]*q[3] - q[0]*q[1] ],
                        [q[1]*q[3] - q[0]*q[2], q[0]*q[1] - q[2]*q[3], q[0]**2 + q[3]**2 - 0.5 ] ])
        return 2*Ro

    def Euler2RoMat(ro):
        Rx = np.array([ [1.,              0.,               0.],
                        [0., math.cos(ro[0]), -math.sin(ro[0])],
                        [0., math.sin(ro[0]),  math.cos(ro[0])] ])
        Ry = np.array([ [ math.cos(ro[1]), 0., math.sin(ro[1])],
                        [              0., 1.,              0.],
                        [-math.sin(ro[1]), 0., math.cos(ro[1])] ])
        Rz = np.array([ [math.cos(ro[2]), -math.sin(ro[2]), 0.],
                        [math.sin(ro[2]),  math.cos(ro[2]), 0.],
                        [             0.,               0., 1.] ])
        Ro = np.array(Rz.dot(Ry)).dot(Rx)
        return Ro

    def TFMat(tr, Ro):
        tmp = np.append( np.array(Ro.dot(np.eye(3, 4))), np.array([[0., 0., 0., 1.]]), axis=0 )
        Tr = np.array([ [1., 0., 0., tr[0]],
                        [0., 1., 0., tr[1]],
                        [0., 0., 1., tr[2]],
                        [0., 0., 0., 1.]    ])
        T = Tr.dot(tmp)

        return T

    def Inverse(m):
        m_T = m.T
        mT = np.linalg.inv(m_T.dot(m)).dot(m_T)
        return mT


class Frame(object):
    # Z-Y-X
    def __init__(self, position=(0., 0., 0.), orientation=(0., 0., 0.), timestamp=None):
        if (len(position) != 3):
            raise IOError()
        if (len(orientation) != 3):
            raise IOError()
        #self.Reset()

        self._time = t()
        m = TF.TFMat(position, TF.Euler2RoMat(orientation))
        if timestamp is None:
            self._t = np.array([self._time.now()])
        else:
            self._t = np.array([timestamp])
        self._m = np.array([m])

    def ResetMat(self, m, timestamp=None):
        if timestamp is None:
            self._t = np.array([self._time.now()])
        else:
            self._t = np.array([timestamp])
        self._m = np.array([m])

        return self

    def dot(self, T, timestamp=None):
        m = self._m[-1]
        if ( isinstance(T, Frame) ):
            m = m.dot(T.m())
        else:
            m = m.dot(T)

        if timestamp is None:
            self._t = np.append(self._t, self._time.now())
        else:
            self._t = np.append(self._t, timestamp)
        self._m = np.concatenate( (self._m, np.array([m])), axis=0)

    def UpdateMat(self, m, timestamp=None):
        if ( isinstance(m, Frame) ):
            m = m.m()

        if timestamp is None:
            self._t = np.append(self._t, self._time.now())
        else:
            self._t = np.append(self._t, timestamp)
        self._m = np.concatenate( (self._m, np.array([m])), axis=0)

    def UpdateTrRo(self, pos, rpy, timestamp=None):
        m = TF.TFMat(pos, TF.Euler2RoMat(rpy))

        if timestamp is None:
            self._t = np.append(self._t, self._time.now())
        else:
            self._t = np.append(self._t, timestamp)
        self._m = np.concatenate( (self._m, np.array([m])), axis=0)

    def Inverse(self):
        return TF.Inverse(self._m[-1])

    def Transformation(self, trans, rpy, timestamp=None):
        T = TF.TFMat(trans, TF.Euler2RoMat(rpy))
        return self.dot(T, timestamp)

    def Translate(self, trans, timestamp=None):
        T = TF.TFMat(trans, TF.Euler2RoMat(np.array([0.0, 0.0, 0.0])))
        return self.dot(T, timestamp)

    def RotateRoll(self, theta, timestamp=None):
        T = TF.TFMat(np.array([0.0, 0.0, 0.0]), TF.Euler2RoMat(np.array([theta, 0.0, 0.0])))
        return self.dot(T, timestamp)

    def RotatePitch(self, theta, timestamp=None):
        T = TF.TFMat(np.array([0.0, 0.0, 0.0]), TF.Euler2RoMat(np.array([0.0, theta, 0.0])))
        return self.dot(T, timestamp)

    def RotateYaw(self, theta, timestamp=None):
        T = TF.TFMat(np.array([0.0, 0.0, 0.0]), TF.Euler2RoMat(np.array([0.0, 0.0, theta])))
        return self.dot(T, timestamp)

    def x(self):
        return self._m[-1][0][3]
    def y(self):
        return self._m[-1][1][3]
    def z(self):
        return self._m[-1][2][3]
    def m(self):
        return self._m[-1]
    def t(self):
        return self._t[-1]
    def timespace(self):
        return self._t
    def M(self):
        return self._m

    def pos(self):
        return np.array([self._m[-1][0][3], self._m[-1][1][3], self._m[-1][2][3]])
    def rpy(self):
        return TF.RoMat2Euler(self._m[-1])
    def quat(self):
        return TF.RoMat2Quat(self._m[-1])


###
class _Tree(object):
    dict = {}
    node = {}
    tree = {}

class Tree(object):
    def __init__(self):
        self.Tree = _Tree()
        if not bool(self.Tree.tree):
            self.Tree.dict['origin'] = Frame( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) )
            self.Tree.node['origin'] = 'origin'
            self.Tree.tree['origin'] = []
        return

    def Node(self, name):
        return self.Tree.dict[name]

    def AddNode(self, name, obj, parent='origin'):
        if name in self.Tree.node:
            return
        self.Tree.node[name] = parent
        self.Tree.dict[name] = obj
        self.Tree.tree[parent].append(name)
        self.Tree.tree[name] = []

    def _RecursiveSearch(self, A, B):
        list = []
        if A not in B:
            list.extend( self._RecursiveSearch(self.Tree.node[A], B) )
            list.extend([A])
            return list
        else:
            return [B[B.index(A)]]

    def SearchTwoFrame(self, A, B):
        list_A = self._RecursiveSearch(A, ['origin'])
        list_B = self._RecursiveSearch(B, list_A)
        list = [[], [], []]

        T = np.eye(4)
        for i in range(len(list_A) - 1, list_A.index(list_B[0]), -1):
            list[0].append(list_A[i])

        list[1].append(list_B[0])
        for i in range(1, len(list_B)):
            list[2].append(list_B[i])

        return list

    def Dis2T(self, list):
        T = np.eye(4)
        for name in list[0]:
            T_T = self.Tree.dict[name].Inverse()
            T = T.dot(T_T)

        for name in list[2]:
            T = T.dot(self.Tree.dict[name].m())

        return Frame().ResetMat(T)

    def TwoFrame(self, A, B):
        #from A to B
        list = self.SearchTwoFrame(A, B)

        return self.Dis2T(list), list

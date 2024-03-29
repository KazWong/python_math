import numpy as np
import math
import time
import threading

from ..protobuf import tf_tree_pb2

class t:
    #class for share time, update in Time class
    s_step = 0
    ns_step = 0
    count = 0
    s = []
    ns = []

    def now(self):
        if (self.s):
            return self.s[-1] + (self.ns[-1] / 1.e9)
        else:
            return None

    def timespace(self):
        if (self.s):
            return np.array(self.s) + (np.array(self.ns) / 1.e9)
        else:
            return None

    def step(self):
        return self.s_step + (self.ns_step / 1.e9)


###
class Time:
    # Simulation Time
    # step: floating point in sec

    def __init__(self, step):
        self.time = t()
        self.SetTick(step)

    def Reset(self):
        t.count = 0
        self._rt = 0
        self.time.s.clear()
        self.time.ns.clear()

    def SetTick(self, step):
        if (step <= 0.0):
            raise AssertionError('Step <= 0.0')
        t.s_step = np.round(float(step))
        t.ns_step = (float(step) - t.s_step)*1e9

    def Offline(self, end_time):
        # end_time: floating point of end time in sec, -1 is infinity for Online tick, Offline return error
        if (end_time < 0.0):
            raise AssertionError('Offline mode end time < 0.0')
        if (end_time > self.now()):
            step = self.step()

            start = self.now()
            if (start > 0.0):
                start += step
            if (np.around(math.fmod(end_time+start, step), 9) == 0.0):
                end_time = end_time + self.step()/2.0
            else:
                end_time = end_time + self.step()
            [self.Tick() for _ in np.arange(start, end_time, step)]
        return self.timespace()

    def Tick(self):
        if (not self.time.s):
            self.time.s.append(0)
            self.time.ns.append(0)
        else:
            t.count += 1
            s = self.time.s[-1] + t.s_step
            ns = self.time.ns[-1] + t.ns_step
            if (ns > 1e9):
                s += 1
                ns -= 1e9
            self.time.s.append(s)
            self.time.ns.append(ns)

    def RealTick(self):
        if (not self.time.s):
            self._rt = time.monotonic()
            self.time.s.append(0)
            self.time.ns.append(0)
        else:
            t.count += 1
            rt = time.monotonic() - self._rt
            self.time.s.append(math.floor(rt))
            self.time.ns.append((rt - math.floor(rt))*1e9)

    def step(self):
        return self.time.step()

    def Len(self):
        return len(self.time.s)

    def now(self):
        if (self.time.now() is None):
            return 0.0
        return self.time.now()

    def timespace(self):
        return self.time.timespace()

    def count(self):
        return t.count


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
        self._T = self._time.step()
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

        if (self._T == self._time.step()):
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
# S.Saraband, F.Thomas, "Accurate Computation ofQuaternions from Rotation Matrices" http://www.iri.upc.edu/files/scidoc/2068-Accurate-Computation-of-Quaternions-from-Rotation-Matrices.pdf
# Yan-Bin Jia, "Quaternions and Rotations" https://www.weizmann.ac.il/sci-tea/benari/sites/sci-tea.benari/files/uploads/softwareAndLearningMaterials/quaternion-tutorial-2-0-1.pdf
# Moti Ben-Ari, "A Tutorial on Euler Angles and Quaternions" http://graphics.stanford.edu/courses/cs348a-17-winter/Papers/quaternion.pdf
# K.Groÿekatthöfer, Z.Yoon, "Intro ductionintoquaternionsforspacecraftattituderepresentation" http://www.tu-berlin.de/fileadmin/fg169/miscellaneous/Quaternions.pdf
class TF(object):
    # Euler: Z-Y-X
    # Quat: w x y z
    def Euler2Quat(orien):
        Qx = np.array([[math.cos(orien[0]/2.), 0., 0.], [math.sin(orien[0]/2.), 0.0,                   0.0]])
        Qy = np.array([[math.cos(orien[1]/2.), 0., 0.], [0.0,                   math.sin(orien[1]/2.), 0.0]])
        Qz = np.array([[math.cos(orien[2]/2.), 0., 0.], [0.0,                   0.0,                   math.sin(orien[2]/2.)]])

        ### Quaternion product
        Qzy = np.array([np.array([Qz[0][0]*Qy[0][0] - Qz[1].dot(Qy[1]), 0., 0.]), np.array([Qz[0][0]*Qy[1] + Qy[0][0]*Qz[1] + np.cross(Qz[1], Qy[1])])])
        Q = np.array([Qzy[0][0]*Qx[0][0] - Qzy[1].dot(Qx[1])])
        Q = np.append(Q, Qzy[0][0]*Qx[1] + Qx[0][0]*Qzy[1] + np.cross(Qzy[1], Qx[1]))

        return Q

    def RoMat2Tran(m):
        return np.array([m[0][3], m[1][3], m[2][3]])

    def RoMat2Quat(m):
        eff = 0.0

        tmp = m[0][0] + m[1][1] + m[2][2]
        if (tmp > eff):
            q0 = math.sqrt( (1. + tmp) ) /2.
        else:
            q0 = math.sqrt( ( (m[2][1]-m[1][2])**2 + (m[0][2]-m[2][0])**2 + (m[1][0]-m[0][1])**2 )/(3. - tmp) ) /2.
        tmp = m[0][0] - m[1][1] - m[2][2]
        if (tmp > eff):
            q1 = math.sqrt( (1. + tmp) ) /2.
        else:
            q1 = math.sqrt( ( (m[2][1]-m[1][2])**2 + (m[0][1]+m[1][0])**2 + (m[2][0]+m[0][2])**2 )/(3. - tmp) ) /2.
        tmp = -m[0][0] + m[1][1] - m[2][2]
        if (tmp > eff):
            q2 = math.sqrt( (1. + tmp) ) /2.
        else:
            q2 = math.sqrt( ( (m[0][2]-m[2][0])**2 + (m[0][1]+m[1][0])**2 + (m[1][2]+m[2][1])**2 )/(3. - tmp) ) /2.
        tmp = -m[0][0] - m[1][1] + m[2][2]
        if (tmp > eff):
            q3 = math.sqrt( (1. + tmp) ) /2.
        else:
            q3 = math.sqrt( ( (m[1][0]-m[0][1])**2 + (m[2][0]+m[0][2])**2 + (m[2][1]+m[1][2])**2 )/(3. - tmp) ) /2.

        return np.array([q0, q1, q2, q3])

    def RoMat2Euler(m):
        r =  math.atan2(m[2][1], m[2][2])
        p = -math.asin(m[2][0])
        y =  math.atan2(m[1][0], m[0][0])
        return np.array([r, p, y])

    def Quat2RoMat(quat):
        #homogeneous expression
        q = quat
        Ro = np.array([ [q[0]**2 + q[1]**2 - 0.5, q[1]*q[2] - q[0]*q[3], q[1]*q[3] + q[0]*q[2] ],
                        [q[1]*q[2] + q[0]*q[3], q[0]**2 + q[2]**2 - 0.5, q[2]*q[3] - q[0]*q[1] ],
                        [q[1]*q[3] - q[0]*q[2], q[2]*q[3] + q[0]*q[1], q[0]**2 + q[3]**2 - 0.5 ] ])
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
    # Quat: w x y z
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
        self._proto = None

    def Proto(self, proto):
        self._proto = proto
        self._SetProto(TF.RoMat2Tran(self._m[-1]), TF.RoMat2Quat(self._m[-1]))

    def _SetProto(self, pos, quat):
        self._proto.p.x = pos[0]
        self._proto.p.y = pos[1]
        self._proto.p.z = pos[2]
        self._proto.q.w = quat[0]
        self._proto.q.x = quat[1]
        self._proto.q.y = quat[2]
        self._proto.q.z = quat[3]

    def ResetMat(self, m, timestamp=None):
        if timestamp is None:
            self._t = np.array([self._time.now()])
        else:
            self._t = np.array([timestamp])
        self._m = np.array([m])
        if self._proto:
            self._SetProto(TF.RoMat2Tran(self._m[-1]), TF.RoMat2Quat(self._m[-1]))
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
        if self._proto:
            self._SetProto(TF.RoMat2Tran(self._m[-1]), TF.RoMat2Quat(self._m[-1]))

    def UpdateMat(self, m, timestamp=None):
        if ( isinstance(m, Frame) ):
            m = m.m()

        if timestamp is None:
            self._t = np.append(self._t, self._time.now())
        else:
            self._t = np.append(self._t, timestamp)
        self._m = np.concatenate( (self._m, np.array([m])), axis=0)
        if self._proto:
            self._SetProto(TF.RoMat2Tran(self._m[-1]), TF.RoMat2Quat(self._m[-1]))

    def UpdateTrRo(self, pos, rpy, timestamp=None):
        m = TF.TFMat(pos, TF.Euler2RoMat(rpy))

        if timestamp is None:
            self._t = np.append(self._t, self._time.now())
        else:
            self._t = np.append(self._t, timestamp)
        self._m = np.concatenate( (self._m, np.array([m])), axis=0)
        if self._proto:
            self._SetProto(TF.RoMat2Tran(self._m[-1]), TF.RoMat2Quat(self._m[-1]))

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
    def proto(self):
        return self._proto

    def pos(self):
        return np.array([self._m[-1][0][3], self._m[-1][1][3], self._m[-1][2][3]])
    def rpy(self):
        return TF.RoMat2Euler(self._m[-1])
    def quat(self):
        return TF.RoMat2Quat(self._m[-1])
    def Ro(self):
        m34 = np.eye(3, 4);m43 = np.eye(4, 3)
        return m34.dot(self._m[-1]).dot(m43)


###
class TTree(object):
    tree = tf_tree_pb2.Tree()
    dict = {}
    _lock = threading.Lock()

class Tree(object):
    def __init__(self):
        self.Tree = TTree()
        if not bool(self.Tree.dict):
            self.Tree._lock.acquire()
            self.Tree.dict['origin'] = Frame( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) )
            self.Tree.tree.node['origin'].parent = 'origin'
            self.Tree.dict['origin'].Proto(self.Tree.tree.node['origin'].tf)
            self.Tree._lock.release()
        return

    def Node(self, name):
        return self.Tree.dict[name]

    def AddNode(self, name, obj, parent='origin'):
        self.Tree._lock.acquire()
        if name in self.Tree.tree.node:
            self.Tree._lock.release()
            return
        self.Tree.tree.node[name].parent = parent
        self.Tree.dict[name] = obj
        self.Tree.dict[name].Proto(self.Tree.tree.node[name].tf)
        self.Tree.tree.node[parent].child.extend([name])
        self.Tree._lock.release()

    def _RecursiveSearch(self, A, B):
        list = []
        if A not in B:
            self.Tree._lock.acquire()
            AA = self.Tree.tree.node[A].parent
            self.Tree._lock.release()
            list.extend( self._RecursiveSearch(AA, B) )
            list.extend([A])
            return list
        else:
            return [B[B.index(A)]]

    def SearchTwoFrame(self, A, B):
        list_A = self._RecursiveSearch(A, ['origin'])
        list_B = self._RecursiveSearch(B, list_A)
        list = [[], [], []]

        T = np.eye(4)
        list_A_index = list_A.index(list_B[0])
        for i in range(len(list_A) - 1, list_A_index, -1):
            list[0].append(list_A[i])

        list[1].append(list_B[0])
        for i in range(1, len(list_B)):
            list[2].append(list_B[i])

        return list

    def Dis2T(self, list):
        T = np.eye(4)
        for name in list[0]:
            self.Tree._lock.acquire()
            T_T = self.Tree.dict[name].Inverse()
            self.Tree._lock.release()
            T = T.dot(T_T)

        for name in list[2]:
            self.Tree._lock.acquire()
            T = T.dot(self.Tree.dict[name].m())
            self.Tree._lock.release()

        return Frame().ResetMat(T)

    def TwoFrame(self, A, B):
        #from A to B
        list = self.SearchTwoFrame(A, B)

        return self.Dis2T(list), list

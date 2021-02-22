import numpy as np
import math
import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from ..dynamic_systems.motion import Translation1D, Rotation1D
from ..simtools import *
from ..simtools.plotlib import *

print('********************************************************************')
print('')
print('Frame & TF:')

TEST_COUNT = 0

### TF Function
print('\tTest TF function\t', end =" ");TEST_COUNT += 1
ro_rx = np.array([ [-1.0,  0.0,  0.0],
                   [ 0.0, -1.0,  0.0],
                   [ 0.0,  0.0,  1.0]])
ro_mm = np.array([ [ 0.1368536, -0.7023747,  0.6985277],
                   [ 0.8668462,  0.4261976,  0.2587148],
                   [-0.4794255,  0.5701100,  0.6671775]])
mm_aa = np.array([ [ 3.0, -2.0,  4.0],
                   [ 1.0,  0.0,  2.0],
                   [ 0.0,  1.0,  0.0]])
aa_mm = np.array([ [ 1.0, -2.0,  2.0],
                   [ 0.0,  0.0,  1.0],
                   [-0.5,  1.5, -1.0]])

if ( (np.around(TF.Euler2Quat(np.array([0.5, 1.2, 0.13])), 7) != np.array([0.807063, 0.1682243, 0.5591969, -0.0874573])).any() ):
    print('TF: Fail in ', TEST_COUNT, '-1')
    print('euler: ', np.array([0.5, 1.2, 0.13]))
    print('Euler2Quat:  ', np.around(TF.Euler2Quat(np.array([0.5, 1.2, 0.13])), 7))
    print('quat: ', np.array([0.807063, 0.1682243, 0.5591969, -0.0874573]))
    raise AssertionError()
if ( (TF.RoMat2Quat(ro_rx) != np.array([0.0, 0.0, 0.0, 1.0])).any() ):
    print('TF: Fail in ', TEST_COUNT, '-2')
    print('RoMat:  ', TF.RoMat2Quat(ro_rx))
    print('quat: ', np.array([0.0, 0.0, 0.0, 1.0]))
    raise AssertionError()
if ( (np.around(TF.RoMat2Euler(ro_rx), 7) != np.array([0.0, 0.0, 3.1415927])).any() ):
    print('TF: Fail in ', TEST_COUNT, '-3')
    print('RoMat:  ', np.around(TF.RoMat2Euler(ro_rx), 7))
    print('euler: ', np.array([0.0, 0.0, 3.1415927]))
    raise AssertionError()
if ( (np.around(TF.Quat2RoMat(np.array([0.7466975, 0.1042575, 0.3943877, 0.5253871])), 7) != ro_mm).any() ):
    print('TF: Fail in ', TEST_COUNT, '-4')
    print('RoMat: ', np.around(TF.Quat2RoMat(np.array([0.7466975, 0.1042575, 0.3943877, 0.5253871])), 7))
    print('RoMat:  ', ro_mm)
    raise AssertionError()
if ( (np.around(TF.Euler2RoMat(np.array([0.70710667, 0.5, 1.41421343])), 7) != ro_mm).any() ):
    print('TF: Fail in ', TEST_COUNT, '-5')
    print('RoMat: ', np.around(TF.Euler2RoMat(np.array([0.70710667, 0.5, 1.41421343])), 7))
    print('RoMat:  ', ro_mm)
    raise AssertionError()
if ( (np.around(TF.Inverse(mm_aa), 2) != aa_mm).any() ):
    print('TF: Fail in ', TEST_COUNT, '-6')
    print('RoMat: ', mm_aa)
    print('RoMat: ', np.around(TF.Inverse(mm_aa), 2))
    print('RoMat:  ', aa_mm)
    raise AssertionError()
print('Pass')

### Frame init & output
print('\tTest Frame init output\t', end =" ");TEST_COUNT += 1
origin = Frame()
t1 = Frame([1.0, 2.0, 3.0], [0.1, 0.2, 0.3])
ro_t1 = np.array([ [ 0.9362934, -0.2750958,  0.2183507],
                   [ 0.2896295,  0.9564251, -0.0369570],
                   [-0.1986693,  0.0978434,  0.9751703] ])

if ( (origin.pos() != np.array([0.0, 0.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-1')
    print('origin:  ', origin.pos())
    print('pos: ', [0.0, 0.0, 0.0])
    raise AssertionError()
if ( (origin.rpy() != np.array([0.0, 0.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-2')
    print('origin:  ', origin.rpy())
    print('rpy: ', [0.0, 0.0, 0.0])
    raise AssertionError()
if ( (t1.pos() != np.array([1.0, 2.0, 3.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-3')
    print('t1:  ', t1.pos())
    print('pos: ', [1.0, 2.0, 3.0])
    raise AssertionError()
if ( (np.around(t1.rpy(), 9) != np.array([0.1, 0.2, 0.3])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-4')
    print('t1:  ', t1.rpy())
    print('rpy: ', np.array([0.1, 0.2, 0.3]))
    raise AssertionError()
if ( (np.around(origin.quat(), 9) != np.array([1.0, 0.0, 0.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-5')
    print('origin rpy:  ', origin.rpy())
    print('origin T:  \n', origin.m())
    print('origin Ro:  \n', origin.Ro())
    print('origin quat:  ', origin.quat())
    print('quat: ', np.array([1.0, 0.0, 0.0, 0.0]))
    raise AssertionError()
if ( (np.around(t1.quat(), 7) != np.array([0.9833474, 0.0342708, 0.1060205, 0.1435722])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-6')
    print('t1 rpy:  ', t1.rpy())
    print('t1 T:  \n', t1.m())
    print('t1 Ro:  \n', t1.Ro())
    print('t1 quat:  ', t1.quat())
    print('quat: ', np.array([0.9833474, 0.0342708, 0.1060205, 0.1435722]))
    raise AssertionError()
if ( t1.x() != 1.0 ):
    print('Frame: Fail in ', TEST_COUNT, '-7')
    print('t1 x:  ', t1.x())
    print('x: ', 1.0)
    raise AssertionError()
if ( t1.y() != 2.0 ):
    print('Frame: Fail in ', TEST_COUNT, '-8')
    print('t1 x:  ', t1.y())
    print('x: ', 2.0)
    raise AssertionError()
if ( t1.z() != 3.0 ):
    print('Frame: Fail in ', TEST_COUNT, '-9')
    print('t1 x:  ', t1.z())
    print('x: ', 3.0)
    raise AssertionError()
if ( t1.t() is not None ):
    print('Frame: Fail in ', TEST_COUNT, '-10')
    print('t1 t:  ', t1.t())
    print('t: ', None)
    raise AssertionError()
if ( t1.timespace() != [None] ):
    print('Frame: Fail in ', TEST_COUNT, '-11')
    print('t1 timespace:  ', t1.timespace())
    print('timespace: ', [None])
    raise AssertionError()
if ( (np.around(t1.Ro(), 7) != ro_t1).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-12')
    print('t1 rotation matrix:  ', (np.around(t1.Ro(), 7)))
    print('ro: ', ro_t1)
    raise AssertionError()
print('Pass')

### Frame init & output
print('\tTest Frame update\t', end =" ");TEST_COUNT += 1
sampling_rate = 1000.;end_time = 0.1
clock = Time(1./sampling_rate)
origin = Frame()
dx = [1.0, 0.0, 0.0]
ro_rx = np.array([ [-1.0,  0.0,  0.0, 1.0],
                   [ 0.0, -1.0,  0.0, 2.0],
                   [ 0.0,  0.0,  1.0, 2.0],
                   [ 0.0,  0.0,  0.0, 1.0] ])
tr_dx = np.array([ [ 1.0,  0.0,  0.0, 1.0],
                   [ 0.0,  1.0,  0.0, 0.0],
                   [ 0.0,  0.0,  1.0, 0.0],
                   [ 0.0,  0.0,  0.0, 1.0] ])

if ( origin.t() is not None ):
    print('Frame: Fail in ', TEST_COUNT, '-1')
    print('origin t:  ', origin.t())
    print('t: ', None)
    raise AssertionError()
if ( origin.timespace() != [None] ):
    print('Frame: Fail in ', TEST_COUNT, '-2')
    print('origin timespace:  ', origin.timespace())
    print('timespace: ', [None])
    raise AssertionError()
clock.Tick()
origin = Frame()
if ( origin.t() != 0.0 ):
    print('Frame: Fail in ', TEST_COUNT, '-3')
    print('origin t:  ', origin.t())
    print('t: ', 0.0)
    raise AssertionError()
if ( origin.timespace() != [0.0] ):
    print('Frame: Fail in ', TEST_COUNT, '-4')
    print('origin timespace:  ', origin.timespace())
    print('timespace: ', [0.0])
    raise AssertionError()
clock.Tick()
origin.UpdateTrRo(dx, np.array([0.0, 0.0, 0.0]))
if ( (origin.pos() != np.array([1.0, 0.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-5')
    print('origin:  ', origin.pos())
    print('pos: ', [1.0, 0.0, 0.0])
    raise AssertionError()
if ( origin.t() != 0.001 ):
    print('Frame: Fail in ', TEST_COUNT, '-6')
    print('origin t:  ', origin.t())
    print('t: ', 0.001)
    raise AssertionError()
clock.Tick()
origin.UpdateMat(ro_rx)
if ( (origin.pos() != np.array([1.0, 2.0, 2.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-7')
    print('origin:  ', origin.pos())
    print('pos: ', [1.0, 2.0, 2.0])
    raise AssertionError()
if ( (np.around(origin.rpy(), 7) != np.array([0.0, 0.0, 3.1415927])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-8')
    print('origin:  ', np.around(origin.rpy(), 7))
    print('rpy: ', np.array([0.0, 0.0, 3.1415927]))
    raise AssertionError()
clock.Tick()
t1 = Frame()
t1.dot(tr_dx)
if ( (t1.pos() != np.array([1.0, 0.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-9')
    print('t1:  ', t1.pos())
    print('pos: ', [1.0, 0.0, 0.0])
    raise AssertionError()
if ( (t1.rpy() != np.array([0.0, 0.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-10')
    print('t1:  ', t1.rpy())
    print('rpy: ', np.array([0.0, 0.0, 0.0]))
    raise AssertionError()
tr = Frame().ResetMat(ro_rx)
t1.dot(tr)
t1_tr = np.array([ [-1.0,  0.0,  0.0, 2.0],
                   [ 0.0, -1.0,  0.0, 2.0],
                   [ 0.0,  0.0,  1.0, 2.0],
                   [ 0.0,  0.0,  0.0, 1.0] ])
if ( (t1.pos() != np.array([2.0, 2.0, 2.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-11')
    print('t1:  ', t1.pos())
    print('pos: ', [2.0, 2.0, 2.0])
    raise AssertionError()
if ( (np.around(t1.rpy(), 7) != np.array([0.0, 0.0, 3.1415927])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-12')
    print('t1:  ', t1.rpy())
    print('rpy: ', np.array([0.0, 0.0, 3.1415927]))
    raise AssertionError()
if ( (np.around(t1.m(), 7) != t1_tr).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-13')
    print('t1:  ', t1.rpy())
    print('rpy: ', np.array([0.0, 0.0, 3.1415927]))
    raise AssertionError()
tr = Frame().ResetMat(ro_rx)

print('Pass')

print()


### set plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

x0 = Frame([0., 0., 0.], [0., 0., 0.])
xx0 = Frame([0., 0., 0.], [0., 0., 0.])
x1 = Frame([1., 0., 0.], [0., 0., 0.])
x2 = Frame([-1., 0., 0.], [0., 0., 0.])
x3 = Frame([0., -1., 0.], [0., 0., 0.])
dx = [0.5, 0.0, 0.0]
dxx = [0.5, 0.2, 0.0]
r0 = [0.0, 0.0, 0.0]
r = [0.0, 0.0, -math.pi/4]

#Frame(x1.pos(), x1.rpy())
#Frame(x2.pos(), x2.rpy())
#Frame(x3.pos(), x3.rpy())

PlotFrame(ax, x0)
plt.scatter(x0.x(), x0.y(), c='r', s=10.0)

x0.Translate(dx)
PlotPose(ax, x0.pos(), x0.rpy())
plt.scatter(x0.x(), x0.y(), c='b', s=10.0)

x0.RotateYaw(r[2])
PlotFrame(ax, x0)
plt.scatter(x0.x(), x0.y(), c='g', s=10.0)

x0.Translate(dx)
PlotPose(ax, x0.pos(), x0.rpy())
plt.scatter(x0.x(), x0.y(), c='g', s=10.0)

xx0.Transformation(dxx, r)
PlotFrame(ax, xx0)
plt.scatter(xx0.x(), xx0.y(), c='m', s=10.0)

xx0.Transformation(dxx, r)
PlotPose(ax, xx0.pos(), xx0.rpy())
plt.scatter(xx0.x(), xx0.y(), c='m', s=10.0)

if (len(sys.argv) > 1):
    if (bool(sys.argv[1]) is True):
        plt.show()

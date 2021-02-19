import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from ..dynamic_systems.motion import Translation1D, Rotation1D
from ..simtools import *
from ..simtools.plotlib import *

print('********************************************************************')
print('')
print('Frame & TF:')

TEST_COUNT = 0

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
t1_tr = np.array([ [ 1.0,  0.0,  0.0, 1.0],
                   [ 0.0,  1.0,  0.0, 0.0],
                   [ 0.0,  0.0,  1.0, 0.0],
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
tr = Frame().ResetMat(ro_rx)

print('Pass')

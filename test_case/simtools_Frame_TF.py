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

### Frame init
print('\tTest Frame init\t\t', end =" ");TEST_COUNT += 1
origin = Frame()
t1 = Frame([1.0, 2.0, 3.0], [0.1, 0.2, 0.3])

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
print('Pass')

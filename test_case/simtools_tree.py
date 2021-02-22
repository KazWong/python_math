import numpy as np
import math
import sys
from ..simtools import *
from ..simtools.plotlib import *


print('********************************************************************')
print('')
print('Tree:')

TEST_COUNT = 0



### TF Tree
print('\tTest init\t\t', end =" ");TEST_COUNT += 1
tf = Tree()
tf.AddNode('map', Frame( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) ))
tf.AddNode('r0', Frame( np.array([0.5, 1.0, 0.0]), np.array([0.0, 0.0, -math.pi/2.]) ), 'map')

if ( (tf.Node('map').pos() != np.array([0.0, 0.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-1')
    print('map:  ', tf.Node('map').pos())
    print('pos: ', [0.0, 0.0, 0.0])
    raise AssertionError()
if ( (tf.Node('r0').pos() != np.array([0.5, 1.0, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-2')
    print('map:  ', tf.Node('r0').pos())
    print('pos: ', [0.5, 1.0, 0.0])
    raise AssertionError()
print('Pass')


### TF between two Frame
print('\tTest TwoFrame\t\t', end =" ");TEST_COUNT += 1

tf.AddNode('r0_w0', Frame( np.array([0.5, 0.5, 0.0]), np.array([0.0, 0.0, -math.pi/2.]) ), 'r0')
tf.AddNode('r1', Frame( np.array([-3.0, -1.0, 0.0]), np.array([0.0, 0.0, -3.*math.pi]) ), 'map')
tf.AddNode('r1_bd', Frame( np.array([1.0, 0.5, 0.0]), np.array([0.0, 0.0, math.pi*3./4.]) ), 'r1')
tf.AddNode('r1_w0', Frame( np.array([0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')

r1_w0_orig, r1_w0_L = tf.TwoFrame('origin', 'r1_w0')
r1_w0_pos = r1_w0_orig.pos()
r1_w0_rpy = r1_w0_orig.rpy()

r0_w0_orig, r0_w0_L = tf.TwoFrame('origin', 'r0_w0')
r0_w0_pos = r0_w0_orig.pos()
r0_w0_rpy = r0_w0_orig.rpy()

T, L = tf.TwoFrame('r1_w0', 'r0_w0')

if ( (np.around(r0_w0_pos, 8) != np.array([1.0, 0.5, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-1')
    print('r0_w0:  ', r0_w0_pos)
    print('pos: ', [1.0, 0.5, 0.0])
    raise AssertionError()
if ( (np.around(r1_w0_pos, 8) != np.array([-3.29289322, -1.5, 0.0])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-2')
    print('r1_w0:  ', r1_w0_pos)
    print('pos: ', [-3.29289322, -1.5, 0.0])
    raise AssertionError()
if ( (L != np.array([['r1_w0', 'r1_bd', 'r1'], ['map'], ['r0', 'r0_w0']])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-3')
    print('L:  ', L)
    print('pos: ', np.array([['r1_w0', 'r1_bd', 'r1'], ['map'], ['r0', 'r0_w0']]))
    raise AssertionError()
if ( (r1_w0_L != np.array([[], ['origin'], ['map', 'r1', 'r1_bd', 'r1_w0']])).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-4')
    print('r1_w0_L:  ', r1_w0_L)
    print('pos: ', np.array([[], ['origin'], ['map', 'r1', 'r1_bd', 'r1_w0']]))
    raise AssertionError()
if ( (tf.Dis2T(L).m() != T.m()).any() ):
    print('Frame: Fail in ', TEST_COUNT, '-3')
    print('L:  ', tf.Dis2T(L).m())
    print('T: ', T.m())
    raise AssertionError()
print('Pass')

tf.AddNode('r1_w0_2', Frame( np.array([r1_w0_pos[0], r1_w0_pos[1], 1.0]), r1_w0_rpy ))
tf.AddNode('r0_w0_2', Frame( np.array([r0_w0_pos[0], r0_w0_pos[1], 0.5]), r0_w0_rpy ))

### From r1_w0_2 to r0_w0
tf.AddNode('r0_w0_T', Frame(), 'r1_w0_2')
tf.Node('r0_w0_T').ResetMat( T.m() )

### From origin to r0_w0
tf.AddNode('r0_w0_3', Frame())
tf.Node('r0_w0_3').ResetMat( tf.Node('r1_w0_2').m().dot(T.m()) )
tf.Node('r0_w0_3').Translate([0.0, 0.0, 0.5])


tf.AddNode('r0_w1', Frame( np.array([0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')
tf.AddNode('r0_w2', Frame( np.array([-0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')
tf.AddNode('r0_w3', Frame( np.array([-0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')

tf.AddNode('r1_w1', Frame( np.array([0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w2', Frame( np.array([-0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w3', Frame( np.array([-0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


tf.AddNode('r1_w0_2', Frame( np.array([r1_w0_pos[0], r1_w0_pos[1], 1.0]), r1_w0_rpy ))
tf.AddNode('r0_w0_2', Frame( np.array([r0_w0_pos[0], r0_w0_pos[1], 0.5]), r0_w0_rpy ))
PlotFrame(ax, tf.Node('r1_w0_2'), 'r1_w0_2')
PlotPoseHeading(tf.Node('r1_w0_2').pos(), tf.Node('r1_w0_2').rpy(), T.m())

### From r1_w0_2 to r0_w0
tf.AddNode('r0_w0_T', Frame(), 'r1_w0_2')
tf.Node('r0_w0_T').ResetMat( T.m() )

### From origin to r0_w0
tf.AddNode('r0_w0_3', Frame())
tf.Node('r0_w0_3').ResetMat( tf.Node('r1_w0_2').m().dot(T.m()) )
tf.Node('r0_w0_3').Translate([0.0, 0.0, 0.5])

tf2 = Tree()

PlotFrame(ax, r1_w0_orig, 'r1_w0')
PlotFrame(ax, r0_w0_orig, 'r0_w0')
PlotFrame(ax, tf.Node('r0_w0_2'), 'r0_w0_2')
PlotFrame(ax, tf.Node('r0_w0_T'), 'r0_w0_T - This is correct, apply T from origin')
PlotFrame(ax, tf.Node('r0_w0_3'), 'r0_w0_3')


PlotHeading(r1_w0_orig, T)

SetPlotOrigin(ax, r1_w0_pos, 3)



fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

SetPlotOrigin(ax, tf.Node('r1_w0_2').pos(), 3)

PlotTree(ax)


print()

if (len(sys.argv) > 1):
    if (bool(sys.argv[1]) is True):
        plt.show()

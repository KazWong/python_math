import numpy as np
import math

from ..simtools import *
from ..simtools.plotlib import *

sampling_rate = 1000.;end_time = 5.
clock = Time(1./sampling_rate)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')



### TF Tree
tf = Tree()
tf.AddNode('map', Frame( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) ))

tf.AddNode('r0', Frame( np.array([0.5, 1.0, 0.0]), np.array([0.0, 0.0, -math.pi/4.]) ), 'map')
tf.AddNode('r0_w0', Frame( np.array([0.5, 0.5, 0.0]), np.array([0.0, 0.0, math.pi/2.]) ), 'r0')
tf.AddNode('r0_w1', Frame( np.array([0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')
tf.AddNode('r0_w2', Frame( np.array([-0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')
tf.AddNode('r0_w3', Frame( np.array([-0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')


tf.AddNode('r1', Frame( np.array([1.0, 6.0, 0.0]), np.array([0.0, 0.0, -3.*math.pi]) ), 'map')
tf.AddNode('r1_bd', Frame( np.array([1.0, 0.5, 0.0]), np.array([0.0, 0.0, math.pi*3./4.]) ), 'r1')
tf.AddNode('r1_w0', Frame( np.array([0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w1', Frame( np.array([0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w2', Frame( np.array([-0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w3', Frame( np.array([-0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')

print(tf.Node('origin').pos())
print(tf.Node('r0').pos())

print('origin: ', tf.Tree.node['origin'])
print('r0: ', tf.Tree.node['r0'])
print('r1_w0: ', tf.Tree.node['r1_w0'])
print('r1: ', tf.Tree.node['r1'])

print('TREE: ', tf.Tree.node)
print('TREE: ', tf.Tree.tree)
print()

T, L = tf.TwoFrame('r1_w0', 'r0_w0')

r1_w0_orig, r1_w0_L = tf.TwoFrame('origin', 'r1_w0')
r1_w0_pos = r1_w0_orig.pos()
r1_w0_rpy = r1_w0_orig.rpy()

r0_w0_orig, r0_w0_L = tf.TwoFrame('origin', 'r0_w0')
r0_w0_pos = r0_w0_orig.pos()
r0_w0_rpy = r0_w0_orig.rpy()

#print(L)
#print(T)

tf.AddNode('r1_w0_2', Frame( np.array([r1_w0_pos[0] + 1.0, r1_w0_pos[1], 0.0]), r1_w0_orig.rpy() ))
PlotFrame(ax, tf.Node('r1_w0_2'), 'r1_w0_2_1')
PlotPoseHeading(tf.Node('r1_w0_2').pos(), tf.Node('r1_w0_2').rpy(), T.m())
tf.Node('r1_w0_2').dot(T)

tf2 = Tree()
print("tf2", tf2.Node('r1_w0_2').pos())
print('TREE tf2: ', tf.Tree.tree)
print('TREE tf2: ', tf.Tree.node)
print()

PlotFrame(ax, r1_w0_orig, 'r1_w0')
PlotFrame(ax, r0_w0_orig, 'r0_w0')
PlotFrame(ax, tf2.Node('r1_w0_2'), 'r1_w0_2_2')

PlotHeading(r1_w0_orig, T)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(-2, 2)

PlotTree(ax)

plt.show()

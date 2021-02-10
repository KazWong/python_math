import numpy as np
import math
import matplotlib.pyplot as plt
from ..simtools import *
from ..simtools.plotlib import *

sampling_rate = 1000.;end_time = 5.
clock = Time(1./sampling_rate)

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal')        # Set aspect ratio
plt.xlim(-8, 8)                    # Set x-axis range
plt.ylim(-8, 8)                    # Set y-axis range


### TF Tree
tf = Tree()
tf.AddNode('map', Transform( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) ))

tf.AddNode('r0', Transform( np.array([0.5, 1.0, 0.0]), np.array([0.0, 0.0, -math.pi/4.]) ), 'map')
tf.AddNode('r0_w0', Transform( np.array([0.5, 0.5, 0.0]), np.array([0.0, 0.0, math.pi/2.]) ), 'r0')
tf.AddNode('r0_w1', Transform( np.array([0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')
tf.AddNode('r0_w2', Transform( np.array([-0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')
tf.AddNode('r0_w3', Transform( np.array([-0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r0')


tf.AddNode('r1', Transform( np.array([1.0, 6.0, 0.0]), np.array([0.0, 0.0, -3.*math.pi]) ), 'map')
tf.AddNode('r1_bd', Transform( np.array([1.0, 0.5, 0.0]), np.array([0.0, 0.0, math.pi*3./4.]) ), 'r1')
tf.AddNode('r1_w0', Transform( np.array([0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w1', Transform( np.array([0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w2', Transform( np.array([-0.5, 0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')
tf.AddNode('r1_w3', Transform( np.array([-0.5, -0.5, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'r1_bd')

print(tf.Node('origin').pos())
print(tf.Node('r0').pos())

print('origin: ', tf.Tree.node['origin'])
print('r0: ', tf.Tree.node['r0'])
print('r1_w0: ', tf.Tree.node['r1_w0'])
print('r1: ', tf.Tree.node['r1'])

print('TREE: ', tf.Tree.node)
print('TREE: ', tf.Tree.tree)
print()

T, L = tf.Transformation('r1_w0', 'r0_w0')

r1_w0_T, r1_w0_L = tf.Transformation('origin', 'r1_w0')
r1_w0_pos = np.array([r1_w0_T[0][3], r1_w0_T[1][3]])
r1_w0_orien = np.array([math.atan2(r1_w0_T[2][1], r1_w0_T[2][2]), -math.asin(r1_w0_T[2][0]), math.atan2(r1_w0_T[1][0], r1_w0_T[0][0])])

r0_w0_T, r0_w0_L = tf.Transformation('origin', 'r0_w0')
r0_w0_pos = np.array([r0_w0_T[0][3], r0_w0_T[1][3]])
r0_w0_orien = np.array([math.atan2(r0_w0_T[2][1], r0_w0_T[2][2]), -math.asin(r0_w0_T[2][0]), math.atan2(r0_w0_T[1][0], r0_w0_T[0][0])])

#print(L)
#print(T)

tf.AddNode('r1_w0_2', Transform( np.array([r1_w0_pos[0] + 1.0, r1_w0_pos[1], 0.0]), np.array([r1_w0_orien[0], r1_w0_orien[1], r1_w0_orien[2]]) ))
Frame(tf.Node('r1_w0_2').pos(), tf.Node('r1_w0_2').orien(), 'r1_w0_2')
tf.Node('r1_w0_2').Transformation( np.array([T[0][3], T[1][3], 0.0]), np.array([0.0, 0.0, math.atan2(T[1][0], T[0][0])]) )

tf2 = Tree()
print("tf2", tf2.Node('r1_w0_2').pos())
print('TREE tf2: ', tf.Tree.tree)
print('TREE tf2: ', tf.Tree.node)
print()

Frame(r1_w0_pos, r1_w0_orien, 'r1_w0')
Frame(r0_w0_pos, r0_w0_orien, 'r0_w0')
Frame(tf.Node('r1_w0_2').pos(), tf.Node('r1_w0_2').orien(), 'r1_w0_2')

Heading(r1_w0_pos, r1_w0_orien, T)

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal')        # Set aspect ratio
plt.xlim(-10, 10)                    # Set x-axis range
plt.ylim(-10, 10)                    # Set y-axis range

PlotTree()

plt.show()

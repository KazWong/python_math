import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from ..dynamic_systems.motion import Translation1D, Rotation1D
from ..motion_profile.vaj import Motion_vaj
from ..simtools import *
from ..simtools.plotlib import *

#time
sampling_rate = 1000.
clock = Time(1./sampling_rate)

#space
tf = Tree()
obj_3d = [Translation1D(), Translation1D(), Translation1D(), Rotation1D(), Rotation1D(), Rotation1D()] #x, y, z, rx, ry, rz
tf.AddNode('map', Frame( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) ))
tf.AddNode('odom', Frame( np.array([0.3, 0.7, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'map')
tf.AddNode('base_footprint', Frame( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'odom')
tf.AddNode('wheel_FR', Frame( np.array([0.5, -0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
tf.AddNode('wheel_FL', Frame( np.array([0.5, 0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
tf.AddNode('wheel_BR', Frame( np.array([-0.5, -0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
tf.AddNode('wheel_BL', Frame( np.array([-0.5, 0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
tf.AddNode('base_link', Frame( np.array([0.0, 0.0, 0.7]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
tf.AddNode('cam_base', Frame( np.array([0.4, 0.0, 0.2]), np.array([0.0, 0.0, 0.0]) ), 'base_link')
tf.AddNode('cam_R', Frame( np.array([0.0, -0.15, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'cam_base')
tf.AddNode('cam_L', Frame( np.array([0.0, 0.15, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'cam_base')
fig = plt.figure()
plt.xlabel('x')
plt.ylabel('y')
ax = fig.gca(projection='3d')
#PlotTree()
PlotFrame(ax, tf.Node('base_footprint'), 'base_footprint')


x0 = [0., 0., 0., 0.]
xn1 = [5., 0., 0.]
xn = [-3., 0., 0.]
T1 = 10.
T2 = 36.

"""
u0 = Motion_vaj(T1, x0[1:], xn1)
u = [0.0, 0.0, 0.0]
u_1 = [0.0, 0.0, 0.0]

clock.Reset()
while (clock.now() < T1):
    clock.Tick()
    u_1 = u0.Update()
    obj.Update( np.array([u_1 - u]) )
    u = u_1

x0 = obj.y()
u1 = Motion_vaj(T2-T1, x0[1:], xn)
u1.t_shift(-clock.now())
while (clock.now() < T2):
    clock.Tick()
    u_1 = u1.Update()
    obj.Update( np.array([u_1 - u]) )
    u = u_1

y = obj.Y()
y = y.reshape([-1, 4])

pos = u0.Pos()
pos = np.append(pos, u1.Pos())
t = u0.timespace()
t = np.append(t, u1.timespace())

plt.figure()
plt.suptitle('1D Motion')
plt.subplot(411)
plt.xlabel('t')
plt.ylabel('pos')
plt.plot(clock.timespace(), y[:,0])
plt.subplot(412)
plt.xlabel('t')
plt.ylabel('vel')
plt.plot(clock.timespace(), y[:,1])
plt.subplot(413)
plt.xlabel('t')
plt.ylabel('acc')
plt.plot(clock.timespace(), y[:,2])
plt.subplot(414)
plt.xlabel('t')
plt.ylabel('jerk')
plt.plot(clock.timespace(), y[:,3])


x0 = Transform([0., 0., 0.], [0., 0., 0.])

plt.figure()
for i in range(clock.Len()):
    dx = [y[i,0], 0.0, 0.0]
    x0.Translate(dx)
    Frame(x0.pos(), x0.orien())
"""
plt.show()

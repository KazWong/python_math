import time
import numpy as np
import threading
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ..dynamic_systems.motion import Translation1D, Rotation1D
from ..motion_profile.linear import VAJ
from ..simtools import *
from ..simtools.plotlib import *
from ..ros import *

sampling_rate = 100.
clock = Time(1./sampling_rate)
tf = Tree()
alive = True

def RoboTF():
    tf.AddNode('map', Frame( np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]) ))
    tf.AddNode('odom', Frame( np.array([0.3, 0.7, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'map')
    tf.AddNode('base_footprint', Frame( np.array([0.2, 0.2, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'odom')
    tf.AddNode('wheel_FR', Frame( np.array([0.5, -0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
    tf.AddNode('wheel_FL', Frame( np.array([0.5, 0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
    tf.AddNode('wheel_BR', Frame( np.array([-0.5, -0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
    tf.AddNode('wheel_BL', Frame( np.array([-0.5, 0.25, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
    tf.AddNode('base_link', Frame( np.array([0.0, 0.0, 0.7]), np.array([0.0, 0.0, 0.0]) ), 'base_footprint')
    tf.AddNode('cam_base', Frame( np.array([0.4, 0.0, 0.2]), np.array([0.0, 0.0, 0.0]) ), 'base_link')
    tf.AddNode('cam_R', Frame( np.array([0.0, -0.15, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'cam_base')
    tf.AddNode('cam_L', Frame( np.array([0.0, 0.15, 0.0]), np.array([0.0, 0.0, 0.0]) ), 'cam_base')

def PlotRobo():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    base_footprint_orig, base_footprint_L = tf.TwoFrame('origin', 'base_footprint')
    SetPlotOrigin(ax, base_footprint_orig.pos(), 1.2)
    PlotTree(ax)

def update(frame, axis):
    ani = Tree_Quiver()

    base_footprint_orig, base_footprint_L = tf.TwoFrame('origin', 'base_footprint')
    base_footprint_orig = tf.Dis2T(base_footprint_L)
    SetPlotOrigin(axis, base_footprint_orig.pos(), 0.5)
    AniTree(axis)
    text.set_text(str("time = " + str(np.around(clock.now(), 3))))

    return ani.tree.values()

def Sim():
    global alive
    T = 30.
    # x
    xx0 = [0., 0., 0., 0.]
    xxn = [10., 0.8, 0., 0.]
    # y
    xy0 = [0., 0., 0., 0.]
    xyn = [2., 1.2, 0., 0.]
    # z
    xz0 = [0., 0., 0., 0.]
    xzn = [15., 0., 0., 0.]
    obj_3d = [Translation1D(), Translation1D(), Translation1D()] #x, y, z, rx, ry, rz
    u_3d = [VAJ(T, xx0[1:], xxn[1:]), VAJ(T, xy0[1:], xyn[1:]), VAJ(T, xz0[1:], xzn[1:])]
    u = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    x = 0.0
    y = 0.0
    z = 0.0

    clock.Reset()

    while alive:
        clock.RealTick()
        for i in range(3):
            u_1 = u_3d[i].Update()
            obj_3d[i].Update(np.array([u_1 - u[i]]))
            u[i] = u_1
            x_1 = obj_3d[0].x()[0]
            y_1 = obj_3d[1].x()[0]
            z_1 = obj_3d[2].x()[0]

            T1 = TF.TFMat(np.array([x_1 - x, y_1 - y, z_1 - z]), np.eye(3))
            tf.Node('base_footprint').dot(T1)

            x = x_1
            y = y_1
            z = z_1


if __name__ == '__main__':
    RoboTF()

    th_sim = threading.Thread(target=Sim)
    th_sim.start()

    sync_tf = Sync_ROS_TF()

    fig = plt.figure()
    #axis = fig.gca(projection='3d')

    #axis.set_xlabel('x')
    #axis.set_ylabel('y')
    #axis.set_zlabel('z')
    #text = axis.text2D(0.0, 0.0, str("time = " + str(clock.now())), transform=axis.transAxes)
    #anim = FuncAnimation(fig, update, fargs=(axis, ), frames=20, interval=20, blit=False)
    plt.show()

    alive = False
    th_sim.join()

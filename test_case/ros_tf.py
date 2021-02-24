import time
import numpy as np
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


def main():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    base_footprint_orig, base_footprint_L = tf.TwoFrame('origin', 'base_footprint')
    SetPlotOrigin(ax, base_footprint_orig.pos(), 1.2)
    PlotTree(ax)

if __name__ == '__main__':
    RoboTF()

    main()

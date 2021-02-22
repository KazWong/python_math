import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from ..simtools import *

class Setting:
    arrow_len = 0.1
    head_width = 0.02
    head_length = 1.5 * head_width

def SetPlotOrigin(ax, pos, range):
    ax.set_xlim(pos[0]-range,pos[0]+range)
    ax.set_ylim(pos[1]-range,pos[1]+range)
    ax.set_zlim(pos[2]-range,pos[2]+range)

def PlotFrame(ax, frame, name=None):
    s = Setting()
    origin = frame.pos()

    xhat = frame.Ro().dot(np.array([s.arrow_len, 0, 0]))
    yhat = frame.Ro().dot(np.array([0, s.arrow_len, 0]))
    zhat = frame.Ro().dot(np.array([0, 0, s.arrow_len]))

    plt.quiver(*origin, *xhat, color='r')
    plt.quiver(*origin, *yhat, color='g')
    plt.quiver(*origin, *zhat, color='b')
    if (name):
        ax.text(origin[0] + 0.02, origin[1], origin[2], name)

def PlotHeading(frame, T):
    origin = frame.pos()
    vector = T.pos()
    vector = frame.Ro().dot(vector)
    plt.quiver(*origin, *vector, color='y', arrow_length_ratio=0.05)

def PlotPose(ax, pos, orien, name=None):
    s = Setting()
    origin = np.array([pos[0], pos[1], pos[2]])
    Ro = TF.Euler2RoMat(orien)

    xhat = Ro.dot(np.array([s.arrow_len, 0, 0]))
    yhat = Ro.dot(np.array([0, s.arrow_len, 0]))
    zhat = Ro.dot(np.array([0, 0, s.arrow_len]))

    plt.quiver(*origin, *xhat, color='r')
    plt.quiver(*origin, *yhat, color='g')
    plt.quiver(*origin, *zhat, color='b')
    if (name):
        ax.text(origin[0] + 0.02, origin[1], origin[2], name)

def PlotPoseHeading(orig, orien, trans):
    frame = Frame(orig, orien)
    origin = frame.pos()
    vector = np.array([trans[0][3], trans[1][3], trans[2][3]])
    vector = frame.Ro().dot(vector)
    plt.quiver(*origin, *vector, color='y', arrow_length_ratio=0.05)

def PlotTree(ax, name='origin', T=None):
    tf = Tree()
    if T is None:
        T = np.eye(4)

    for i in tf.Tree.tree[name]:
        if i:
            total_trans = T.dot(tf.Node(name).m())
            PlotTree(ax, i, total_trans)

    pose = T.dot(tf.Node(name).m())
    pose_pos = np.array([pose[0][3], pose[1][3], pose[2][3]])
    pose_orien = TF.RoMat2Euler(pose)
    PlotPose(ax, pose_pos, pose_orien, name)

    head = T
    head_pos = np.array([head[0][3], head[1][3], head[2][3]])
    head_orien = TF.RoMat2Euler(head)
    if (tf.Node(name).m() == np.eye(4)).all():
        return
    PlotPoseHeading(head_pos, head_orien, tf.Node(name).m())

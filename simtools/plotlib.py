import numpy as np
import math
import matplotlib.pyplot as plt
from ..simtools import *

class Setting:
    arrow_len = 0.1
    head_width = 0.02
    head_length = 1.5 * head_width

def PlotFrame(ax, frame, name=None):
    s = Setting()
    origin = frame.pos()
    xhat = np.array([s.arrow_len, 0, 0])
    yhat = np.array([0, s.arrow_len, 0])
    zhat = np.array([0, 0, s.arrow_len])


    rz = frame.rpy()[2]
    # BUG: Orientation
    R = np.array([[math.cos(rz), -math.sin(rz), 0],
                  [math.sin(rz), math.cos(rz), 0],
                  [0, 0, 1]])
    new_xhat = R.dot(xhat)
    new_yhat = R.dot(yhat)
    new_zhat = R.dot(zhat)

    plt.quiver(*origin, *new_xhat, color='r')
    plt.quiver(*origin, *new_yhat, color='g')
    plt.quiver(*origin, *new_zhat, color='b')
    if (name):
        ax.text(origin[0] + 0.02, origin[1], origin[2], name)

def PlotHeading(frame, T):
    s = Setting()
    origin = frame.pos()
    trans = T.pos()

    # BUG: Orientation
    theta = frame.rpy() + T.rpy()
    len = math.sqrt(trans[0]**2 + trans[1]**2 + trans[2]**2)
    translation = np.array([len*np.cos(theta), len*np.sin(theta)])
    plt.quiver(*origin, *translation, color='y')

def PlotPose(pos, orien, name=None):
    s = Setting()
    origin = np.array([pos[0], pos[1], pos[2]])
    xhat = np.array([s.arrow_len, 0, 0])
    yhat = np.array([0, s.arrow_len, 0])
    zhat = np.array([0, 0, s.arrow_len])

    # BUG: Orientation
    R = np.array([[math.cos(rz), -math.sin(rz), 0],
                  [math.sin(rz), math.cos(rz), 0],
                  [0, 0, 1]])
    new_xhat = R.dot(xhat)
    new_yhat = R.dot(yhat)
    new_zhat = R.dot(zhat)

    plt.quiver(*origin, *new_xhat, color='r')
    plt.quiver(*origin, *new_yhat, color='g')
    plt.quiver(*origin, *new_zhat, color='b')
    if (name):
        ax.text(origin[0] + 0.02, origin[1], origin[2], name)

def PlotPoseHeading(orig, orien, trans):
    s = Setting()
    origin = np.array([orig[0], orig[1]])

    # BUG: Orientation
    theta = orien[2] + math.atan2(trans[1][3], trans[0][3])
    len = math.sqrt(trans[0][3]**2 + trans[1][3]**2) - s.head_length
    translation = np.array([len*np.cos(theta), len*np.sin(theta)])
    plt.arrow(*origin, *translation, head_width=s.head_width, head_length=s.head_length, color='y')

def PlotTree(name='origin', T=None):
    tf = Tree()
    if T is None:
        T = np.eye(4)

    for i in tf.Tree.tree[name]:
        if i:
            total_trans = T.dot(tf.Node(name).m())
            PlotTree(i, total_trans)

    pose = T.dot(tf.Node(name).m())
    pose_pos = np.array([pose[0][3], pose[1][3]])
    pose_orien = np.array([math.atan2(pose[2][1], pose[2][2]), -math.asin(pose[2][0]), math.atan2(pose[1][0], pose[0][0])])
    PlotPose(pose_pos, pose_orien, name)

    head = T
    head_pos = np.array([head[0][3], head[1][3]])
    head_orien = np.array([math.atan2(head[2][1], head[2][2]), -math.asin(head[2][0]), math.atan2(head[1][0], head[0][0])])
    if (tf.Node(name).m() == np.eye(4)).all():
        return
    PlotPoseHeading(head_pos, head_orien, tf.Node(name).m())

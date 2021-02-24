import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import matplotlib.pyplot as plt
from ..simtools import *

class Setting:
    arrow_len = 0.1
    head_width = 0.02
    head_length = 1.5 * head_width

class Tree_Quiver(object):
    tree = {}

def SetPlotOrigin(ax, pos, range):
    ax.set_xlim(pos[0]-range,pos[0]+range)
    ax.set_ylim(pos[1]-range,pos[1]+range)
    ax.set_zlim(pos[2]-range,pos[2]+range)

def PlotHeading(frame, T):
    s = Setting()
    origin = frame.pos()
    vector = T.pos()
    vector = frame.Ro().dot(vector)
    len = vector[0]**2 + vector[1]**2 + vector[2]**2
    if (len > 0.0):
        ratio = s.head_length / math.sqrt(len)
    else:
        ratio = 0.0001
    head = plt.quiver(*origin, *vector, color='y', arrow_length_ratio=ratio)
    return head

def PlotPose(ax, pos, orien, name=None, proj22d=False):
    s = Setting()
    ratio = s.head_length / s.arrow_len
    origin = np.array([pos[0], pos[1], pos[2]])
    Ro = TF.Euler2RoMat(orien)

    xhat = Ro.dot(np.array([s.arrow_len, 0, 0]))
    yhat = Ro.dot(np.array([0, s.arrow_len, 0]))
    zhat = Ro.dot(np.array([0, 0, s.arrow_len]))

    qax = ax.quiver(*origin, *xhat, color='r', arrow_length_ratio=ratio)
    qay = ax.quiver(*origin, *yhat, color='g', arrow_length_ratio=ratio)
    qaz = ax.quiver(*origin, *zhat, color='b', arrow_length_ratio=ratio)

    if (name):
        if (proj22d):
            x, y, _ = proj3d.proj_transform(origin[0] + 0.02, origin[1], origin[2], ax.get_proj())
            text = ax.text2D(x, y, name, zorder=1)
        else:
            text = ax.text(origin[0] + 0.02, origin[1], origin[2], name)
        return [qax, qay, qaz, text]
    return [qax, qay, qaz, None]

def PlotFrame(ax, frame, name=None, proj22d=False):
    return PlotPose(ax, frame.pos(), frame.rpy(), name, proj22d)

def PlotPoseHeading(orig, orien, trans):
    frame = Frame(orig, orien)
    T = Frame().ResetMat(trans)
    return PlotHeading(frame, T)

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


def _UpdatePoseX(qa, pos, orien):
    s = Setting()
    origin = np.array([pos[0], pos[1], pos[2]])
    Ro = TF.Euler2RoMat(orien)
    xhat = Ro.dot(np.array([s.arrow_len, 0, 0]))
    qa.set_segments([[[*origin], [*(xhat+origin)]]])

def _UpdatePoseY(qa, pos, orien):
    s = Setting()
    origin = np.array([pos[0], pos[1], pos[2]])
    Ro = TF.Euler2RoMat(orien)
    yhat = Ro.dot(np.array([0, s.arrow_len, 0]))
    qa.set_segments([[[*origin], [*(yhat+origin)]]])

def _UpdatePoseZ(qa, pos, orien):
    s = Setting()
    origin = np.array([pos[0], pos[1], pos[2]])
    Ro = TF.Euler2RoMat(orien)
    zhat = Ro.dot(np.array([0, 0, s.arrow_len]))
    qa.set_segments([[[*origin], [*(zhat+origin)]]])

def _UpdateText(ax, qa, pos, orien):
    x, y, _ = proj3d.proj_transform(pos[0] + 0.02, pos[1], pos[2], ax.get_proj())
    qa.set_position((x, y))

def _UpdateHead(qa, tail, trans):
    head = [trans[0][3], trans[1][3], trans[2][3]]
    qa.set_segments([[[*tail], [*(tail+head)]]])

def AniTree(ax, name='origin', T=None):
    tf = Tree()
    ani = Tree_Quiver()
    if T is None:
        T = np.eye(4)

    for i in tf.Tree.tree[name]:
        if i:
            total_trans = T.dot(tf.Node(name).m())
            AniTree(ax, i, total_trans)

    pose = T.dot(tf.Node(name).m())
    pose_pos = np.array([pose[0][3], pose[1][3], pose[2][3]])
    pose_orien = TF.RoMat2Euler(pose)

    tail = T
    tail_pos = np.array([tail[0][3], tail[1][3], tail[2][3]])
    tail_orien = TF.RoMat2Euler(tail)
    head = tf.Node(name).m()

    n = name + '_x'
    if name + '_x' in ani.tree:
        _UpdatePoseX(ani.tree[name + '_x'], pose_pos, pose_orien)
        _UpdatePoseY(ani.tree[name + '_y'], pose_pos, pose_orien)
        _UpdatePoseZ(ani.tree[name + '_z'], pose_pos, pose_orien)
        _UpdateText(ax, ani.tree[name + '_t'], pose_pos, pose_orien)
        _UpdateHead(ani.tree[name + '_a'], tail_pos, head)
    else:
        qa1 = PlotPoseHeading(tail_pos, tail_orien, head)
        qa = PlotPose(ax, pose_pos, pose_orien, name, True)
        ani.tree[name + '_x'] = qa[0]
        ani.tree[name + '_y'] = qa[1]
        ani.tree[name + '_z'] = qa[2]
        ani.tree[name + '_t'] = qa[3]
        ani.tree[name + '_a'] = qa1

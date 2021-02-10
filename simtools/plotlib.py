import numpy as np
import math
import matplotlib.pyplot as plt
from ..simtools import *

class Setting:
    arrow_len = 0.1
    head_width = 0.02

def PlotFrame(pos, orien, name=None):
    s = Setting()
    origin = np.array([pos[0], pos[1]])
    xhat = np.array([s.arrow_len, 0])
    yhat = np.array([0, s.arrow_len])

    R = np.array([[math.cos(orien[2]), -math.sin(orien[2])],
                  [math.sin(orien[2]), math.cos(orien[2])]])
    new_xhat = R.dot(xhat)
    new_yhat = R.dot(yhat)

    plt.arrow(*origin, *new_xhat, head_width=s.head_width, color='r')
    plt.arrow(*origin, *new_yhat, head_width=s.head_width, color='g')
    if (name):
        plt.text(origin[0] + 0.15, origin[1], name)

def PlotHeading(orig, orien, trans):
    s = Setting()
    origin = np.array([orig[0], orig[1]])

    theta = orien[2] + math.atan2(trans[1][3], trans[0][3])
    len = math.sqrt(trans[0][3]**2 + trans[1][3]**2)
    translation = np.array([len*np.cos(theta), len*np.sin(theta)])
    plt.arrow(*origin, *translation, head_width=s.head_width, color='y')

def PlotTree(name='origin', T=None):
    tf = Tree()
    if T is None:
        T = np.eye(4)

    for i in tf.Tree.tree[name]:
        if i:
            total_trans = T.dot(tf.Node(name).T)
            PlotTree(i, total_trans)

    total_trans = T.dot(tf.Node(name).T)
    pos = np.array([total_trans[0][3], total_trans[1][3]])
    orien = np.array([math.atan2(total_trans[2][1], total_trans[2][2]), -math.asin(total_trans[2][0]), math.atan2(total_trans[1][0], total_trans[0][0])])
    Frame(pos, orien, name)
    Heading(pos, orien, tf.Node(name).Inverse_Matrix(tf.Node(name).T))

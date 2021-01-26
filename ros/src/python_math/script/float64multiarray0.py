#!/usr/bin/env python3

import math
import rospy
import time
import  threading
from std_msgs.msg import Float64MultiArray
from matplotlib.pylab import *
import matplotlib.animation as animation

grid_num = 4

fig = figure(num = 0, figsize=(10,10))
#fig.suptitle("SPEED-OUT feedback")

lock = []
ax = []
for i in range(grid_num):
    lock.append(threading.Lock())
    ax.append(subplot2grid((grid_num, 1), (i, 0)))
tight_layout()

ylim = [4.0, 200.0, 370.0, 1.3]
for i in range(grid_num):
    ax[i].set_ylim(-ylim[i], ylim[i])
    ax[i].set_xlim(0, 20.0)
    ax[i].grid(True)
    ax[i].set_xlabel("t")
    ax[i].set_ylabel("v")

t = [[], [], [], []]
ydata = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
py = [[], [], [], []]

for i in range(grid_num):
    for j in range(grid_num):
        tmp, = ax[i].plot(t[j],ydata[i][j],'b-', label="s")
        py[i].append(tmp)
        tmp, = ax[i].plot(t[j],ydata[i][j],'g-', label="a")
        py[i].append(tmp)
        tmp, = ax[i].plot(t[j],ydata[i][j],'r-', label="v")
        py[i].append(tmp)
        tmp, = ax[i].plot(t[j],ydata[i][j],'m-', label="cmd v")
        py[i].append(tmp)

for i in range(grid_num):
    ax[i].legend([py[i][0],py[i][1],py[i][2],py[i][3]], [py[i][0].get_label(),py[i][1].get_label(),py[i][2].get_label(),py[i][3].get_label()])


t_base = time.time()
t_step = [0.0, 0.0, 0.0, 0.0]

def callback(pos, msg):
  global t, ydata, t_step, t_base

  lock[pos].acquire()
  t[pos] = append(t[pos], t_step[pos])
  for i in range(grid_num):
    ydata[i][pos] = append(ydata[i][pos], msg.data[i])

  if (len(t[pos]) > 11000):
    t[pos] = np.delete(t[pos], 0)
    for i in range(grid_num):
      ydata[i][pos] = np.delete(ydata[i][pos], 0)
  lock[pos].release()

  t_step[pos] = time.time() - t_base

def callback1(msg):
  callback(0, msg)
def callback2(msg):
  callback(1, msg)
def callback3(msg):
  callback(2, msg)
def callback4(msg):
  callback(3, msg)

def update(frame):
  global py, ydata, t

  for i in range(grid_num):
    for j in range(grid_num):
      lock[i].acquire()
      py[j][i].set_data(t[i], ydata[j][i])
      lock[i].release()
    if len(t[i]) > 0 and t[i][-1] >= 17.00:
      lock[i].acquire()
      py[i][3].axes.set_xlim(t[i][-1]-17.0,t[i][-1]+3.0)
      lock[i].release()

  return py[0][0], py[1][0], py[2][0], py[3][0], py[0][1], py[1][1], py[2][1], py[3][1], py[0][2], py[1][2], py[2][2], py[3][2], py[0][4], py[1][4], py[2][4], py[3][4]

if __name__ == '__main__':
  rospy.init_node('multiarray_data', anonymous=True)
  rospy.Subscriber("accel", Float64MultiArray, callback1)
  rospy.Subscriber("omega", Float64MultiArray, callback2)
  rospy.Subscriber("theta", Float64MultiArray, callback3)
  rospy.Subscriber("NONE", Float64MultiArray, callback4)

  ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=False)
  plt.show()
  rospy.spin()

  #try:
  #  Puber()
  #except rospy.ROSInterruptException:
  #  pass

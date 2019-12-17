#!/usr/bin/env python

import math
import rospy
import time
import threading
import tf
import numpy as np
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_axis = 2
y_axis = 1


axis = x_axis * y_axis
fig, ax = plt.subplots(x_axis,y_axis)
lock, ln = [], []
for i in range(axis):
  tmp, = ax[i].plot([], [], animated=True)
  ln.append(tmp)
  lock.append( threading.Lock() )
xdata_f, ydata_f, colors_f = [], [], [] #del x[:]
xdata_b, ydata_b, colors_b = [], [], [] #del x[:]
xdata = [xdata_f, xdata_b]
ydata = [ydata_f, ydata_b]
colors = [colors_f, colors_b]
tf_listener = None #tf.TransformListener()


fig.canvas.set_window_title('Lidar')
ax[0].set_title('Front Lidar')
ax[1].set_title('Back Lidar')

def callback(scan, args):
  xdata = args[0] 
  ydata = args[1]
  colors = args[2]
  lock = args[3]
  target = args[4]
  source = args[5]
  ranges = list(scan.ranges)
  inten = list(scan.intensities)
  
  try:
    (trans, rot) = tf_listener.lookupTransform(target, source, rospy.Time(0))
  except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    pass
  
  x, y, c = np.array([]), np.array([]), np.array([])
  ang = math.atan2(trans[1], trans[0])
  for i in range(len(ranges)):
    if (ranges[i] > scan.range_min and ranges[i] < scan.range_max):
      x = np.append(x, math.cos(scan.angle_min+scan.angle_increment*i) * ranges[i] + trans[0])
      y = np.append(y, math.sin(scan.angle_min+scan.angle_increment*i) * ranges[i] + trans[1])
      c = np.append(c, inten[i]/47)
  
  lock.acquire()
  xdata[:] = x
  ydata[:] = y
  colors[:] = c    
  lock.release()

def init():
  ax[0].set_xlim(-5.0, 5.0)
  ax[0].set_ylim(-5.0, 5.0)
  
  ax[1].set_xlim(-5.0, 5.0)
  ax[1].set_ylim(-5.0, 5.0)
  
  return ln

def update(i):
  for i in range(axis):
    lock[i].acquire()
    ln[i] = ax[i].scatter(xdata[i], ydata[i], s=3, c=colors[i], animated=True)
    lock[i].release()
  return ln
    
if __name__ == '__main__':
  rospy.init_node('lidar_data', anonymous=True)
  tf_listener = tf.TransformListener()
  rospy.Subscriber("front_scan", LaserScan, callback, (xdata_f, ydata_f, colors_f, lock[0], 'front_lidar', 'lidar'))
  rospy.Subscriber("back_scan", LaserScan, callback, (xdata_b, ydata_b, colors_b, lock[1], 'back_lidar', 'lidar'))
  
  ani = FuncAnimation(fig, update, interval=20, init_func=init, blit=True)
  plt.show()
  
  try:
    rospy.spin()
  except rospy.ROSInterruptException:
    pass

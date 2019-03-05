#!/usr/bin/env python

import math
import rospy
import time
import  threading
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

lock = threading.Lock()
fig, ax = plt.subplots()
xdata, ydata, colors = [], [], [] #del x[:]

def callback(scan):
  global xdata, ydata, colors
  ranges = list(scan.ranges)
  inten = list(scan.intensities)
  
  x, y, c = [], [], []
  for i in range(len(ranges)):
    if (ranges[i] > scan.range_min and ranges[i] < scan.range_max):
      y.append(math.cos(scan.angle_min+scan.angle_increment*i) * ranges[i])
      x.append(math.sin(scan.angle_min+scan.angle_increment*i) * ranges[i])
      c.append(inten[i]/47)
  
  lock.acquire()
  xdata = x
  ydata = y
  colors = c
  lock.release()

def init():
  ax.set_xlim(-5.0, 5.0)
  ax.set_ylim(-5.0, 5.0)
  return ax.plot([], [], animated=True)

def update(frame):
  lock.acquire()
  ln = ax.scatter(xdata, ydata, s=3, c=colors, animated=True)
  lock.release()
  return ln,
    
if __name__ == '__main__':
  rospy.init_node('lidar_data', anonymous=True)
  rospy.Subscriber("scan", LaserScan, callback)
  
  ani = FuncAnimation(fig, update, frames=1000, interval=20, init_func=init, blit=True)
  plt.show()
  rospy.spin()
  
  #try:
  #  Puber()
  #except rospy.ROSInterruptException:
  #  pass

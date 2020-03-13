#!/usr/bin/env python3

import math
import rospy
import time
import  threading
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

lock = threading.Lock()
fig, ax = plt.subplots()
xdata, ydata = [], [] #del x[:]
ln, = plt.plot([], [], 'ro', markersize=3, animated=True)

def callback(scan):
  global xdata, ydata
  ranges = list(scan.ranges)
  inten = scan.intensities
  
  x, y = [], []
  for i in range(len(ranges)):
    if (ranges[i] > scan.range_min and ranges[i] < scan.range_max):
      y.append(math.cos(scan.angle_min+scan.angle_increment*i) * ranges[i])
      x.append(math.sin(scan.angle_min+scan.angle_increment*i) * ranges[i])
  
  lock.acquire()
  xdata = x
  ydata = y
  lock.release()

def init():
  ax.set_xlim(-5.0, 5.0)
  ax.set_ylim(-5.0, 5.0)
  return ln,

def update(frame):
  lock.acquire()
  ln.set_data(xdata, ydata)
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

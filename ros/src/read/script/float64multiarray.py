#!/usr/bin/env python3

import math
import rospy
import time
import  threading
from std_msgs.msg import Float64MultiArray
from matplotlib.pylab import *
import matplotlib.animation as animation

lock1 = threading.Lock()
lock2 = threading.Lock()
lock3 = threading.Lock()
lock4 = threading.Lock()

fig = figure(num = 0, figsize=(10,10))
#fig.suptitle("SPEED-OUT feedback")

ax00 = subplot2grid((4, 1), (0, 0))
ax01 = subplot2grid((4, 1), (1, 0))
ax02 = subplot2grid((4, 1), (2, 0))
ax03 = subplot2grid((4, 1), (3, 0))
tight_layout()

t1, t2, t3, t4 = [], [], [], []
y001data, y002data, y003data, y004data = [], [], [], []
y011data, y012data, y013data, y014data = [], [], [], []
y021data, y022data, y023data, y024data = [], [], [], []
y031data, y032data, y033data, y034data = [], [], [], []

ylim = 1.3
ax00.set_ylim(-ylim, ylim)
ax01.set_ylim(-ylim, ylim)
ax02.set_ylim(-ylim, ylim)
ax03.set_ylim(-ylim, ylim)

ax00.set_xlim(0, 20.0)
ax01.set_xlim(0, 20.0)
ax02.set_xlim(0, 20.0)
ax03.set_xlim(0, 20.0)

ax00.grid(True)
ax01.grid(True)
ax02.grid(True)
ax03.grid(True)

ax00.set_xlabel("t")
ax00.set_ylabel("v")
ax01.set_xlabel("t")
ax01.set_ylabel("v")
ax02.set_xlabel("t")
ax02.set_ylabel("v")
ax03.set_xlabel("t")
ax03.set_ylabel("v")

py001, = ax00.plot(t1,y001data,'b-', label="s")
py002, = ax00.plot(t2,y002data,'g-', label="a")
py003, = ax00.plot(t3,y003data,'r-', label="v")
py004, = ax00.plot(t4,y004data,'m-', label="cmd v")
py011, = ax01.plot(t1,y011data,'b-', label="s")
py012, = ax01.plot(t2,y012data,'g-', label="a")
py013, = ax01.plot(t3,y013data,'r-', label="v")
py014, = ax01.plot(t4,y014data,'m-', label="cmd v")
py021, = ax02.plot(t1,y021data,'b-', label="s")
py022, = ax02.plot(t2,y022data,'g-', label="a")
py023, = ax02.plot(t3,y023data,'r-', label="v")
py024, = ax02.plot(t4,y024data,'m-', label="cmd v")
py031, = ax03.plot(t1,y031data,'b-', label="s")
py032, = ax03.plot(t2,y032data,'g-', label="a")
py033, = ax03.plot(t3,y033data,'r-', label="v")
py034, = ax03.plot(t4,y034data,'m-', label="cmd v")


ax00.legend([py001,py002,py003,py004], [py001.get_label(),py002.get_label(),py003.get_label(),py004.get_label()])
ax01.legend([py011,py012,py013,py014], [py011.get_label(),py012.get_label(),py013.get_label(),py014.get_label()])
ax02.legend([py021,py022,py023,py024], [py021.get_label(),py022.get_label(),py023.get_label(),py024.get_label()])
ax03.legend([py031,py032,py033,py034], [py031.get_label(),py032.get_label(),py033.get_label(),py034.get_label()])


t_base = time.time()
t_step_1, t_step_2, t_step_3, t_step_4 = 0.0, 0.0, 0.0, 0.0

def callback1(msg):
  global t1, y001data, y011data, y021data, y031data, t_step_1, t_base  
  
  lock1.acquire()
  t1 = append(t1, t_step_1)
  y001data = append(y001data, msg.data[0])
  y011data = append(y011data, msg.data[1])
  y021data = append(y021data, msg.data[2])
  y031data = append(y031data, msg.data[3])
  lock1.release()
  
  t_step_1 = time.time() - t_base

def callback2(msg):
  global t2, y002data, y012data, y022data, y032data, t_step_2, t_base  
  
  lock2.acquire()
  t2 = append(t2, t_step_2)
  y002data = append(y002data, msg.data[0])
  y012data = append(y012data, msg.data[1])
  y022data = append(y022data, msg.data[2])
  y032data = append(y032data, msg.data[3])
  lock2.release()
  
  t_step_2 = time.time() - t_base

def callback3(msg):
  global t3, y003data, y013data, y023data, y033data, t_step_3, t_base  
  
  lock3.acquire()
  t3 = append(t3, t_step_3)
  y003data = append(y003data, msg.data[0])
  y013data = append(y013data, msg.data[1])
  y023data = append(y023data, msg.data[2])
  y033data = append(y033data, msg.data[3])
  lock3.release()
  
  t_step_3 = time.time() - t_base

def callback4(msg):
  global t4, y004data, y014data, y024data, y034data, t_step_4, t_base  
  
  lock4.acquire()
  t4 = append(t4, t_step_4)
  y004data = append(y004data, msg.data[0])
  y014data = append(y014data, msg.data[1])
  y024data = append(y024data, msg.data[2])
  y034data = append(y034data, msg.data[3])
  lock4.release()
  
  t_step_4 = time.time() - t_base

def update(frame):
  global py001, py011, py021, py031, y001data, y011data, y021data, y031data, t1
  global py002, py012, py022, py032, y002data, y012data, y022data, y032data, t2
  global py003, py013, py023, py033, y003data, y013data, y023data, y033data, t3
  global py004, py014, py024, py034, y004data, y014data, y024data, y034data, t4

  lock1.acquire()
  py001.set_data(t1, y001data)
  py011.set_data(t1, y011data)
  py021.set_data(t1, y021data)
  py031.set_data(t1, y031data)
  lock1.release();
  
  lock2.acquire()
  py002.set_data(t2, y002data)
  py012.set_data(t2, y012data)
  py022.set_data(t2, y022data)
  py032.set_data(t2, y032data)
  lock2.release();
  
  lock3.acquire()
  py003.set_data(t3, y003data)
  py013.set_data(t3, y013data)
  py023.set_data(t3, y023data)
  py033.set_data(t3, y033data)
  lock3.release();
  
  lock4.acquire()
  py004.set_data(t4, y004data)
  py014.set_data(t4, y014data)
  py024.set_data(t4, y024data)
  py034.set_data(t4, y034data)
  if len(t4) > 0 and t4[-1] >= 17.00:
    py004.axes.set_xlim(t4[-1]-17.0,t4[-1]+3.0)
  if len(t4) > 0 and t4[-1] >= 17.00:
    py014.axes.set_xlim(t4[-1]-17.0,t4[-1]+3.0)
  if len(t4) > 0 and t4[-1] >= 17.00:
    py024.axes.set_xlim(t4[-1]-17.0,t4[-1]+3.0)
  if len(t4) > 0 and t4[-1] >= 17.00:
    py034.axes.set_xlim(t4[-1]-17.0,t4[-1]+3.0)
  lock4.release();
		
  return py001, py011, py021, py031, py002, py012, py022, py032, py003, py013, py023, py033, py004, py014, py024, py034
    
if __name__ == '__main__':
  rospy.init_node('multiarray_data', anonymous=True)
  rospy.Subscriber("wheels", Float64MultiArray, callback1)
  rospy.Subscriber("wheels_fba", Float64MultiArray, callback2)
  rospy.Subscriber("wheels_fbv", Float64MultiArray, callback3)
  rospy.Subscriber("wheels_cmdv", Float64MultiArray, callback4)
  
  ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=False)
  plt.show()
  rospy.spin()
  
  #try:
  #  Puber()
  #except rospy.ROSInterruptException:
  #  pass

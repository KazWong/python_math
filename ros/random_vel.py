#!/usr/bin/env python

import rospy
import time
import os
import math
from geometry_msgs.msg import Twist

pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  
def Puber():
  rate = rospy.Rate(30)
  count = 0
  
  twist = Twist()
  twist.linear.x = 0.01
  
  while not rospy.is_shutdown():
    pub.publish(twist)
    if count > 3000:
      twist.linear.x = -twist.linear.x
      count = 0
    count += 1
    rospy.loginfo(twist.linear.x)
    rate.sleep()

if __name__ == '__main__':
  rospy.init_node('Vel_repeater', anonymous=True)
  try:
    Puber()
  except rospy.ROSInterruptException:
    pass
  
  os.system("rostopic pub -1 /cmd_vel geometry_msgs/Twist \"{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: 0.0}}\"")

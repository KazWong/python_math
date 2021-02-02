#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from description.msg import *
from description.srv import *

def callback(bms):
  rospy.loginfo("up something");
  rospy.loginfo(rospy.get_caller_id() + "%f", bms.soc)
  
def listener():
  rospy.init_node('data_listener', anonymous=True)
  
  rospy.Subscriber("battery_state", battery, callback)
  rospy.loginfo("inited")
  rospy.spin()

if __name__ == '__main__':
  listener()

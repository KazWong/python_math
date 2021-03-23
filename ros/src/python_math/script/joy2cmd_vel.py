#!/usr/bin/env python

import numpy as np
import rospy
from sensor_msgs.msg import Joy

def callback(msg):
    print(data.data)
	sys.stdout.flush()

def main():
    rospy.init_node('joy_back', anonymous=True)
    rospy.Subscriber('joy', Joy, callback, queue_size = 1)
    rospy.spin()

if __name__ == '__main__':
    main()

#!/usr/bin/env python

import rospy
import struct
import tf
import math
from geometry_msgs.msg import TransformStamped

def main():
    rospy.init_node('pm_tf', anonymous=True)

    tf = TransformStamped()
    tf_pub = tf.TransformBroadcaster(queue_size=1)

    while not rospy.is_shutdown():
        for line in sys.stdin:
            msg = Proto_msg.TFTree()
            msg.ParseFromString(line.rstrip())

            tf.header.stamp = rospy.Time.now()
            tf.header.frame_id = msg.id
            tf.child_frame_id = msg.p
            tf.transform.translation.x = msg.x
            tf.transform.translation.y = msg.y
            tf.transform.translation.z = msg.z
            tf.transform.rotation.x = msg.q[0]
            tf.transform.rotation.y = msg.q[1]
            tf.transform.rotation.z = msg.q[2]
            tf.transform.rotation.w = msg.q[3]

            tf_pub.sendTransformMessage(tf)

        #rospy.sleep(0.1)

if __name__ == '__main__':
    main()

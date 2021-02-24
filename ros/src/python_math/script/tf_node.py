#!/usr/bin/env python

import rospy
import struct
import tf
import math
from geometry_msgs.msg import TransformStamped
odom_tf = TransformStamped()

def main():
    global odom_msg, odom_tf, vx, vy, vz, x, y, z
    rospy.init_node('can_data', anonymous=True)
    odom_pub = rospy.Publisher('odom', Odometry, queue_size=1)

    current_time = rospy.Time.now()
    last_time = rospy.Time.now()
    tf_pub = tf.TransformBroadcaster(queue_size=1)
    odom_x = 0.0
    odom_y = 0.0
    odom_rz = 0.0

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        #dt = (current_time - last_time).to_sec()

        odom_rz = z #+= vz * dt
        odom_x  = x #x * math.cos(odom_rz) - y * math.sin(odom_rz)
        odom_y  = y #x * math.sin(odom_rz) + y * math.cos(odom_rz)
        quat = tf.transformations.quaternion_from_euler(0.0, 0.0, odom_rz, 'rxyz');

        odom_tf.header.stamp = current_time
        odom_tf.header.frame_id = 'odom'
        odom_tf.child_frame_id = 'base_footprint'
        odom_tf.transform.translation.x = odom_x
        odom_tf.transform.translation.y = odom_y
        odom_tf.transform.translation.z = 0.0
        odom_tf.transform.rotation.x = quat[0]
        odom_tf.transform.rotation.y = quat[1]
        odom_tf.transform.rotation.z = quat[2]
        odom_tf.transform.rotation.w = quat[3]

        last_time = current_time

        tf_pub.sendTransformMessage(odom_tf)

        rospy.sleep(0.1)

if __name__ == '__main__':
    main()

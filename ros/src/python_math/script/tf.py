#!/usr/bin python

import rospy
import struct
import tf2_ros
import math
import time
import tf_tree_pb2
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
import sys

def main():
    rospy.init_node('pm_tf', anonymous=True)

    tf = TransformStamped()
    tf_pub = tf2_ros.TransformBroadcaster()
    odom_msg = Odometry()
    odom_pub = rospy.Publisher('odom', Odometry, queue_size=1)
    msg = tf_tree_pb2.Tree()

    while not rospy.is_shutdown():
        rospy.loginfo('subprocess tf up')
        count = 0
        for line in sys.stdin:
            s = bytearray([chr(ord(_) ^ 0x25) for _ in line.rstrip()])
            print('sub ', len(s))
            sys.stdout.flush()
            if len(s) != 731:
                continue
            if rospy.is_shutdown():
                exit()
            msg.ParseFromString(s)

            for key, value in msg.node.items():
                if str(key) != 'origin':
                    tf.header.stamp = rospy.Time.now()
                    tf.header.seq = count
                    tf.header.frame_id = str(value.parent)
                    tf.child_frame_id = str(key)
                    tf.transform.translation.x = value.tf.p.x
                    tf.transform.translation.y = value.tf.p.y
                    tf.transform.translation.z = value.tf.p.z
                    tf.transform.rotation.x = value.tf.q.x
                    tf.transform.rotation.y = value.tf.q.y
                    tf.transform.rotation.z = value.tf.q.z
                    tf.transform.rotation.w = value.tf.q.w
                    tf_pub.sendTransform(tf)

                if str(key) is 'odom':
                    odom_msg.header.stamp = rospy.Time.now()
                    odom_msg.header.frame_id = str(value.parent)
                    odom_msg.child_frame_id = str(key)
                    odom_msg.pose.pose.position.x = value.tf.p.x
                    odom_msg.pose.pose.position.y = value.tf.p.y
                    odom_msg.pose.pose.position.z = value.tf.p.z
                    odom_msg.pose.pose.orientation.x = value.tf.q.x
                    odom_msg.pose.pose.orientation.y = value.tf.q.y
                    odom_msg.pose.pose.orientation.z = value.tf.q.z
                    odom_msg.pose.pose.orientation.w = value.tf.q.w
                    odom_msg.twist.twist.linear.x  = 0.0
                    odom_msg.twist.twist.linear.y  = 0.0
                    odom_msg.twist.twist.angular.z = 0.0
                    odom_pub.publish(odom_msg)
            count += 1
            time.sleep(0.05)

if __name__ == '__main__':
    main()

from ..simtools import *
from .script import *
import rospy
import tf
import threading

class ROS_TF(object):
    def __init__(self):
        self._thread = threading.Thread(target=self._ros_thread)
        self._thread.start()

    def __del__(self):
        self._thread.join()

    def _ros_thread(self):
        tf = Tree()
        rospy.init_node('ROBO_pub_tf', anonymous=True)
        self._tf_pub = tf.TransformBroadcaster(queue_size=1)

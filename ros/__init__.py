from ..simtools import *
from .script import *
from ..protobuf import tf_tree_pb2
import threading
import sys
import subprocess

class Sync_ROS_TF(object):
    def __init__(self):
        cmd = ['/usr/bin/python2', "python_math/ros/script/tf.py"]
        self._p = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=False)
        self._thread = threading.Thread(target=self._ros_thread)
        self._alive = True
        self._thread.start()

    def __del__(self):
        self._alive = False
        self._p.terminate()
        self._thread.join()

    def _ros_thread(self):
        tree = TTree()

        while self._alive:
            tree._lock.acquire()
            ss = tree.tree.SerializeToString()
            tree._lock.release()
            s = bytes([_ ^ 0x25 for _ in ss]) + b'\n'
            print('pub ', tree.tree.ByteSize(), len(s), flush=True)
            self._p.stdin.write(s)
            self._p.stdin.flush()
            time.sleep(0.05)

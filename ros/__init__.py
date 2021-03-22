from ..simtools import *
from .script import *
import tf
import threading

class Sync_ROS_TF(object):
    def __init__(self):
        self._cmd = [sys.executable, "script/tf.py"]
        self._p = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=False)
        self._thread = threading.Thread(target=self._ros_thread)

    def __del__(self):
        self._p.terminate()
        self._thread.join()

    def _ros_thread(self):
        tf = Tree()

        self._p.stdin.write(s.encode())
        self._p.stdin.flush()

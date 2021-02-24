#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
from std_msgs.msg import Float64MultiArray
import serial
import math
import threading
import tf

ser=serial.Serial('/dev/ttyUSB0',115200,8,'N',1)
sem=threading.Semaphore()

rospy.init_node('read_jy61', anonymous=True)
pub_fba = rospy.Publisher('wheels_fba', Float64MultiArray, queue_size=1)
pub_fbv = rospy.Publisher('wheels_fbv', Float64MultiArray, queue_size=1)
pub_cmdv = rospy.Publisher('wheels_cmdv', Float64MultiArray, queue_size=1)
pub = rospy.Publisher('odom', Odometry, queue_size=1)
odom_broadcaster = tf.TransformBroadcaster()
array_fba = Float64MultiArray()
array_fbv = Float64MultiArray()
array_cmdv = Float64MultiArray()
rate=rospy.Rate(100)
alive = True

def make_odom(vx,vz,x,y,odom_quat,current):
    msg=Odometry()
    msg.header.stamp = current
    msg.header.frame_id = "odom"
    msg.child_frame_id = "base_footprint"

    msg.pose.pose.position=Point(x,y,0.0)
    msg.pose.pose.orientation=Quaternion(*odom_quat)

    vy=0.0

    msg.twist.twist.linear.x=vx
    msg.twist.twist.linear.y=vy
    msg.twist.twist.linear.z=0.0
    msg.twist.twist.angular.x=0.0
    msg.twist.twist.angular.y=0.0
    msg.twist.twist.angular.z=vz
    return msg

def toSerial(data):
    if (not alive):
        sem.acquire()
        ser.write("!VAR 1 0.0\r".encode('utf-8'))
        ser.write("!VAR 2 0.0\r".encode('utf-8'))
        ser.reset_input_buffer()
        sem.release()
        rospy.signal_shutdown("No reason")
        exit()

    x_step=0.015708
    z_step=0.15708
    if abs(data.linear.x)<=0.2 and data.linear.x!=0.0:
        x_tmp=math.ceil(data.linear.x/abs(data.linear.x)*0.2/x_step)
    else:
        x_tmp=math.ceil(data.linear.x/x_step)
    if abs(data.angular.z)<=0.35 and data.angular.z!=0.0:
        z_tmp=math.ceil(data.angular.z/abs(data.angular.z)*0.35/z_step)
    else:
        z_tmp=math.ceil(data.angular.z/z_step)
    x=x_tmp*x_step*100
    z=z_tmp*z_step*100

    command1="!VAR 1 "+str(x)+"\r"
    command2="!VAR 2 "+str(z)+"\r"

    sem.acquire()
    ser.write(command1.encode('utf-8'))
    ser.write(command2.encode('utf-8'))
    ser.reset_input_buffer()
    sem.release()

    #print "Send: ", x, z

def fromSerial(pub,odom_broadcaster,rate):
    global alive

    accel=[0.0, 0.0, 0.0]
    omega=[0.0, 0.0, 0.0]
    theta=[0.0, 0.0, 0.0]
    tempa=[0.0, 0.0, 0.0]
    odom_quat=tf.transformations.quaternion_from_euler(0, 0, 0)
    vx=0.0
    vz=0.0
    while not rospy.is_shutdown():
        try:
            #if ser.in_waiting>=20:
            sem.acquire()
            data=ser.read(size=1)
            sem.release()
                #tmp=data.decode('utf-8')
            if (data == b'\x55'):
                sem.acquire()
                pack=ser.read(size=1)
                sem.release()

                sem.acquire()
                data=ser.read(size=8)
                sem.release()

                if (pack == b'\x51' and len(data)==8):
                    unpacked = struct.unpack('<hhhh', data)
                    accel[0] = unpacked[0]/32768.0*16.0*9.80665
                    accel[1] = unpacked[1]/32768.0*16.0*9.80665
                    accel[2] = unpacked[2]/32768.0*16.0*9.80665
                    tempa[0] = unpacked[3]/340.0+36.53
                if (pack == b'\x52' and len(data)==8):
                    unpacked = struct.unpack('<hhhh', data)
                    omega[0] = unpacked[0]/32768.0*2000.0
                    omega[1] = unpacked[1]/32768.0*2000.0
                    omega[2] = unpacked[2]/32768.0*2000.0
                    tempa[1] = unpacked[3]/340.0+36.53
                if (pack == b'\x53' and len(data)==8):
                    unpacked = struct.unpack('<hhhh', data)
                    theta[0] = unpacked[0]/32768.0*180.0
                    theta[1] = unpacked[1]/32768.0*180.0
                    theta[2] = unpacked[2]/32768.0*180.0
                    tempa[2] = unpacked[3]/340.0+36.53
            print("accel: ", "{:4.6f}".format(accel[0]), "{:4.6f}".format(accel[1]), "{:4.6f}".format(accel[2]))
            print("omega: ", "{:4.6f}".format(omega[0]), "{:4.6f}".format(omega[1]), "{:4.6f}".format(omega[2]))
            print("theta: ", "{:4.6f}".format(theta[0]), "{:4.6f}".format(theta[1]), "{:4.6f}".format(theta[2]))
            print("tempa: ", "{:4.6f}".format(tempa[0]), "{:4.6f}".format(tempa[1]), "{:4.6f}".format(tempa[2]))
            print()

            array_fba.data = [accel[0], omega[0], theta[0], tempa[0]]
            array_fbv.data = [accel[1], omega[1], theta[1], tempa[1]]
            array_cmdv.data = [accel[2], omega[2], theta[2], tempa[2]]
            pub_fba.publish(array_fba)
            pub_fbv.publish(array_fbv)
            pub_cmdv.publish(array_cmdv)
            #current=rospy.Time.now()
            #pub.publish(make_odom(vx,vz,x,y,odom_quat,current))
            #odom_broadcaster.sendTransform((x, y, 0.),odom_quat,current,"base_footprint","odom")
            #rate.sleep()
        except:
            print("***************************Error*****************************")
            print("Shutdown")
            print(sys.exc_info())
            #print "Last Read: ", list
            alive = False
            exit()
def listener():

    sem.acquire()
    ser.write("!VAR 1 0.0\r".encode('utf-8'))
    ser.write("!VAR 2 0.0\r".encode('utf-8'))
    ser.reset_input_buffer()
    sem.release()

    #rospy.Subscriber("cmd_vel_throttle", Twist, toSerial)
    rospy.Subscriber("cmd_vel", Twist, toSerial)

    rospy.spin()

if __name__ == '__main__':
    #arg_list=[pub,odom_broadcaster,rate]
    #t2=threading.Thread(target=fromSerial,args=arg_list)
    #t2.start()
    #listener()
    fromSerial(pub,odom_broadcaster,rate)

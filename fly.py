#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu

class Fly():   
	
    def __init__(self):
        rospy.init_node('fly', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('/crazyflie/cmd_vel', Twist, queue_size=10)
        r = rospy.Rate(200)
	fly_cmd = Twist()
        fly_cmd.linear.z = 50000
        while (not rospy.is_shutdown()):
            self.cmd_vel.publish(fly_cmd)
            r.sleep()

    def shutdown(self):
        rospy.loginfo("Stopping the Crazyflie...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        Fly()
    except:
        rospy.loginfo("fly node terminated.")

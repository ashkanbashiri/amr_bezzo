#!/usr/bin/env python
import rospy
import time
from sensor_msgs.msg import Imu
from crazyflie_driver.srv import UpdateParams
from std_srvs.srv import Empty

class PIDTuner():
    
    def imuSubscriber(self,imu):
        x=0
        #Store Imu data
	
    def __init__(self):
        rospy.init_node('pid_tuner', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        rospy.Subscriber('/crazyflie/imu', Imu, self.imuSubscriber)
        r = rospy.Rate(200)
        #################################################################
	#Initialize PID Gains for Pitch
        rospy.wait_for_service('/crazyflie/update_params')
        rospy.loginfo("found update_params service")
        self.update_params = rospy.ServiceProxy('/crazyflie/update_params', UpdateParams)#Proxy for pushing parameters to crazyflie server
	time.sleep(1)
	#Wait 1 second for the server to catch up
        rospy.set_param("/crazyflie/pid_rate/pitch_kp", 1)
        self.update_params(["pid_rate/pitch_kp"])
	rospy.set_param("/crazyflie/pid_rate/pitch_kd", 0)
        self.update_params(["pid_rate/pitch_kd"])
	rospy.set_param("/crazyflie/pid_rate/pitch_ki", 0)
        self.update_params(["pid_rate/pitch_ki"])

        while (not rospy.is_shutdown()):   
	    
	    rospy.set_param("/crazyflie/pid_rate/pitch_kp", current_kp)
            self.update_params(["pid_rate/pitch_kp"])
	    
	    #IF Oscillating update kd
	    rospy.set_param("/crazyflie/pid_rate/pitch_kd", current_kd)
            self.update_params(["pid_rate/pitch_kd"])
	    time.sleep(2)#wait 1-2 seconds for sampling Imu data
	    
	    #Main Logic Goes here
		#Calculate errors and variation
		#Update proportional and/or derivative gains

   

    def shutdown(self):
        rospy.loginfo("Stopping the pid_tuner...")
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        PIDTuner()
	rospy.spin()
    except:
        rospy.loginfo("pid_tuner node terminated.")

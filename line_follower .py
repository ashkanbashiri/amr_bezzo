#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import SensorState

#global
linear_velocity = 0.0
angular_velocity = 0.0

def processSensing(sensor_data):
    global angular_velocity
    global linear_velocity

    # check the left cliff sensor data
    if( sensor_data.bottom[0] > Value1 ):
	#update linear and angular velocity

    # check the right cliff sensor data 
    if( sensor_data.bottom[2] > Value2 ):
        #update linear and angular velocity

    # check center cliff sensor data, stay on the line
    if( sensor_data.bottom[1] < Value3 ):
        #update linear and angular velocity


   
def run():

	# publish twist messages to /cmd_vel/input.navi
    pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
	#subscribe to sensors/core
    rospy.Subscriber('/mobile_base/sensors/core', SensorState, processSensing)
    rospy.init_node('line_follower')

    global linear_velocity
    global angular_velocity
    linear_velocity = 0.1 #initial linear velocity
    angular_velocity = 0.0
    
    #set initial velocity
    twist = Twist()

    #main loop
    while not rospy.is_shutdown():
        twist.angular.z = angular_velocity
        twist.linear.x = linear_velocity

	# publish the message and delay
        pub.publish(twist)
        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException: pass


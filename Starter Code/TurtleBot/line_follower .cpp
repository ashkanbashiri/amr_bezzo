#include "ros/ros.h"
#include <geometry_msgs/Twist.h>
#include <kobuki_msgs/SensorState.h>
geometry_msgs::Twist vel;

void cliffCallback(const kobuki_msgs::SensorState::ConstPtr& sensorData)
{
  //check left cliff sensor
  if(sensorData->bottom[0] > value1)
  {
      //update vel, turn right
  }

  //check right cliff sensor
  if(sensorData->bottom[2] > value2)
  {
      //update vel, turn left
  }

  //check center cliff sensor
  if(sensorData->bottom[1] < value3)
  {
      //update vel, stay on the line
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "line_follower");
  ros::NodeHandle nh;
  ros::Publisher vel_pub;
  vel_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel_mux/input/navi", 1, true);
  ros::Subscriber sub = nh.subscribe("/mobile_base/sensors/core", 10, cliffCallback);
  ros::Rate loop_rate(10);
  vel.linear.x = 0.1;//linear velocity(m/s)
  vel.angular.z = 0;//angular velocity(rad/s)
  while (ros::ok())
  {
    vel_pub.publish(vel);
    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}


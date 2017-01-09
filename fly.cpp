#include "ros/ros.h"
#include <geometry_msgs/Twist.h>
geometry_msgs::Twist vel;

int main(int argc, char **argv)
{
  ros::init(argc, argv, "fly");
  ros::NodeHandle nh;
  ros::Publisher vel_pub;
  vel_pub = nh.advertise<geometry_msgs::Twist>("/crazyflie/cmd_vel", 1, true);
  ros::Rate loop_rate(200);
  vel.linear.z = 50000;//Set Thrust to fly vertically
  while (ros::ok())
  {
    vel_pub.publish(vel);
    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}


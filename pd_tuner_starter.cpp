#include "ros/ros.h"
#include "sensor_msgs/Imu.h"
#include "crazyflie_driver/UpdateParams.h"
#include "std_srvs/Empty.h"
#include <string>
using namespace std;

void imuCallback(const sensor_msgs::Imu::ConstPtr& imuData)
{
  //Store Imu Data
  
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "pid_tuner");
  ros::NodeHandle nh;
  ros::Publisher vel_pub;
  ros::Subscriber sub = nh.subscribe("/crazyflie/imu", 10, imuCallback);
  ros::Rate loop_rate(200);
  float kp =1;
  float kd =0;
  //Initialize the gains
  ros::ServiceClient client = nh.serviceClient<crazyflie_driver::UpdateParams>("/crazyflie/update_params");
  crazyflie_driver::UpdateParams srv;
  std::vector<std::basic_string<char> > s;
  s.push_back("pid_rate/pitch_kp");
  s.push_back("pid_rate/pitch_kd");
  s.push_back("pid_rate/pitch_ki");
  srv.request.params =s;
  ROS_INFO("Update parameters");
  nh.setParam("/crazyflie/pid_rate/pitch_kp",1);//setting kp gain for pitch controller, update kp if the system is not oscillating yet
  nh.setParam("/crazyflie/pid_rate/pitch_kd",0);//setting kd gain for pitch controller, update kd if oscillating
  nh.setParam("/crazyflie/pid_rate/pitch_ki",0);//setting kd gain for pitch controller, update kd if oscillating
  client.call(srv);
  //Main Loop
  while (ros::ok())
  {
    ROS_INFO("Update parameters");
    nh.setParam("/crazyflie/pid_rate/pitch_kp",kp);//setting kp gain for pitch controller, update kp if the system is not oscillating yet
    nh.setParam("/crazyflie/pid_rate/pitch_kd",kd);//setting kd gain for pitch controller, update kd if oscillating
    client.call(srv);
    //wait 1-2 seconds here to collect imu data
    //Main Logic goes here, calculate errors, update gains
    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}


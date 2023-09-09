## Introduction
Welcome to the software team of Billee!  
This file will have all the information that you need to develop for this team  
Please skim through this file to gain a basic understanding of what we are doing.  
This is meant to be a resource you can go back to if you forget the name of a certain package we are using, or any methodology that we have implemented  

## Hardware
For our computer we are using the Jetson Orin Nano which has the NVIDIA Jetpack packages installed on Ubuntu 20.04  
For image data, depth data, and IMU data, we are using the Intel Realsense D435i  
Other general sensors include encoders and GPS  
We are using the Roboclaw 7x2a for the motor controller (Being reconsidered due to power draw from motors)  

## Software Framework
We are using ROS2 Humble as our software framework  
Currently, it is source installed on our Jetson but this is a tedious way to use ROS and will be transfered to an Ubuntu 22.04 docker at some point  
As a brief description, ROS is a publisher subscriber architecture communicating through a network  

## Movement
The movement code is under the manual_movement package in the organization  
In this package, I set up a publisher which looks at controller inputs and publishes them  
I also set up a subscriber which sees the published inputs and transfers them into motor movement  
This is not the final implementation, as the motor movements should be based on a velocity topic which Nav2 also publishes to  

## Messages
ROS's main form of communication is messages. Each package will need to use messages to function  
If you need to make a specific message, look up the ROS documentation for it and follow the description  
An example of this would be when I made an IMU message using the camera's IMU data for the robot_localization package  

## Autonomous Movement
To start, autonomous movement uses everything based off of transforms  
Transforms are the locations of something relative to the robot's COM (base_link)  
A general overview of these transforms would be: sensor_links -> base_link -> odom -> map -> world  
  
Sensor links are the locations of all the different sensors and you need a transform from each link to base_link  
This is done using Robot_State_Publisher which parses a URDF file to create said transforms  
  
base_link is the location of the robot. This is mainly meant for a centralized location of all sensor links  
It is very important for the link to be located at the robots center of rotation for ease of use  

Odom Link is where it keeps track of your robot's position using Odometry values sent by your sensor links  
I am using robot_localization to mesh all the odometry messages into a single one  
  
Map Link is where it keeps track of all global points of interest like Point Cloud data, LiDAR data, and other things like that  
I am using the Nav2 costmap to create a costmap of all the point cloud data and then also using Nav2 for the navigation packages  
  
World Link is multiple map links connected to each other. This is only useful when you have multiple devices working with each other in unison  
We are not utilizing this link  

To actually move the rover autonomously, we will probably create a custom package which uses the costmap's information and make the rover move accordingly by posting velocity values which the motors should see and accomplish  

## Arm
The arm is being moved through another medium which isnt controlled through ROS at the moment



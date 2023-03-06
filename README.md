# Multile_ROS_node-red

# To run the multiple robots in ROS use the following command. 
   ### Reqiurement
   ROS-Melodic
   ubuntu 18 or above
    
   ### To run the simulation with multiple robots use the following command
   ```
      roslaunch ros_sim multi_turtlebot3_slam_world.launch
   ```
   This will open the gazebo with a ware-house envrionment and will spawn two turtlebot3 robots. 
        
   ### To run the SLAM operation and create the map of the environment. 
   ```
      roslaunch ros_sim multi_turtlebot3_slam.launch   
   ```
   Once we run this, it will open rviz, us ethe 2d navigation arrow for each robot to move the robot and create the map. 
        
   ### The next step is to run the navigation stack for the multiple robots. For this close all the simaultion we ran before and start fresh open terminal and follw the instruction. 
   This will open the gazebo. 
   ```
      roslaunch ros_sim multi_turtlebot3_nav_world.launch   
   ```
   To open the rviz with navigation stack use the following command. 
   ```
      roslaunch ros_sim multi_turtlebot3_navigation.launch   
   ```
   The rviz is opened and now we have to localize the robot, we can see the 2d pose estimate (green arrow) for both the robots, thus using this arrows we can localise      the robot in an given environment. Compare the position in gazebo and try to approximate the position in rviz using the 2D position. 
   While localizing try to move the robots using 2d navigation(purple arrow). 
   Once all the particles converges around the robot, that means the robot is localised accurately. 
   

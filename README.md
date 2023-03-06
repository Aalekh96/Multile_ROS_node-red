# Multile_ROS_node-red

# To run the multiple robots in ROS use the following command. 
   ## reqiurement
   ROS-Melodic
   ubuntu 18 or above
    
   ## To run the simulation with multiple robots use the following command
   ```
      roslaunch ros_sim multi_turtlebot3_slam_world.launch
   ```
   This will open the gazebo with a ware-house envrionment and will spawn two turtlebot3 robots. 
        
   ## To run the SLAM operation and create the map of the environment. 
   '''
   roslaunch multi_turtlebot3_slam.launch
        
   '''
   once we run this, it will open rviz, us ethe 2d navigation arrow for each robot to move the robot and create the map. 
        
   ##
        

cmake_minimum_required(VERSION 3.0.2)
project(wvn_sim)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  xacro
  robot_state_publisher
  rospy
  nav_msgs
  geometry_msgs
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES wvn_sim
#  CATKIN_DEPENDS gazebo_ros xacro robot_state_publisher
#  DEPENDS system_lib
)

# Install directories
install(DIRECTORY launch urdf config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Install Python scripts
catkin_install_python(PROGRAMS scripts/diffbot_state_converter_node.py
                     DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

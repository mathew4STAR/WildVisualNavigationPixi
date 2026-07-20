cmake_minimum_required(VERSION 3.0.2)
project(wvn_sim)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  xacro
  robot_state_publisher
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES wvn_sim
#  CATKIN_DEPENDS gazebo_ros xacro robot_state_publisher
#  DEPENDS system_lib
)

# Install directories
install(DIRECTORY launch urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

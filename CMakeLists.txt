cmake_minimum_required(VERSION 3.5)
#####
# cmake_policy(SET CMP0148 OLD)
#https://github.com/pybind/pybind11/issues/4785
#####
project(zion_zed_ros2_interface)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


#############################################
# Dependencies


# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ZED 3 REQUIRED)
find_package(CUDA REQUIRED)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

#find_package(ament_python REQUIRED)
#find_package(message_generation REQUIRED)
#find_package(message_runtime REQUIRED)
#find_package(sensor_msg REQUIRED)
#find_package(std_msg REQUIRED)
#find_package(zion_msgs REQUIRED)
find_package(nav_msgs REQUIRED) 
find_package(rclcpp REQUIRED) #ROS1->find_package(roscpp REQUIRED)
find_package(rclpy REQUIRED)  #ROS1->find_package(rospy REQUIRED)
find_package(rcutils REQUIRED)
find_package(zed_components REQUIRED)


# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()


###############################################################################
#Add all files in subdirectories of the project in
# a dummy_target so qtcreator have access to all files
file(GLOB_RECURSE all_files ${CMAKE_SOURCE_DIR}/*)
add_custom_target(all_${PROJECT_NAME}_files SOURCES ${all_files})

###############################################################################
# INCLUDES and LIBS
include_directories(
  ${CUDA_INCLUDE_DIRS}
  ${ZED_INCLUDE_DIRS}
  ${CMAKE_CURRENT_SOURCE_DIR}/src
)

###############################################################################
# SOURCES
set(ZED_WRAPPER_SRC
  ${CMAKE_CURRENT_SOURCE_DIR}/src/zed_wrapper.cpp
)

###############################################################################
# Bin and Install

add_executable(zed_wrapper
  ${ZED_WRAPPER_SRC}
)
ament_target_dependencies(zed_wrapper
  rclcpp
  rclcpp_components
  zed_components
)
install(TARGETS zed_wrapper
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY 
  config
  urdf  
  launch
    #launch/zed_camera.launch.py
    
  DESTINATION
    share/${PROJECT_NAME}
)

#ament_python_install_package(${PROJECT_NAME})
ament_package()

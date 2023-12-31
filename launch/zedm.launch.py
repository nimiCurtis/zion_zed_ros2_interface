# Copyright 2022 Stereolabs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    package_name = 'zion_zed_ros2_interface'
    
    # Camera model (force value)
    camera_model = 'zedm'

    # ZED Wrapper node
    zed_wrapper_launch = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource([
            get_package_share_directory(package_name),
            '/launch/include/zed_camera.launch.py'
        ]),
        launch_arguments={
            'camera_model': camera_model
        }.items()
    )

    # return launch file
    return LaunchDescription([
        zed_wrapper_launch
    ])
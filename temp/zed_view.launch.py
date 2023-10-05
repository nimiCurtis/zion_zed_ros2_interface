import os

from ament_index_python.packages import get_package_share_directory


import launch
import launch_ros
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

#from launch import LaunchDescription
#from launch.actions import IncludeLaunchDescription, ExecuteProcess
#from launch.launch_description_sources import PythonLaunchDescriptionSource
#from launch.substitutions import LaunchConfiguration
#from launch_ros.actions import Node



# print(" *******************************************************************************")
# print(" *")
# print(" *     BBBBBBB      IIII   NNN     N   AA       TTTTTTTT   AA")
# print(" *     B      B      II    N N     N   AAA        TTTT     AAA")
# print(" *     B      BB     II    N  N    N   AAAA        TT      AAAA")
# print(" *     BBBBBBBBB     II    N   N   N   AAAAA       TT      AAAAA")
# print(" *     B        BB   II    N   N   N   AA   A      TT      AA   A")
# print(" *     B        BB   II    N    N  N   AA    A     TT      AA    A")
# print(" *     BBBBBBBBBB   IIII   N    NNNN   AA     A   TTTT     AA     A")
# print(" *")
# print(" *******************************************************************************")
# print(" * All software (C, py, C++)")
# print(" *******************************************************************************")
# time.sleep(1)

# print("")
# print("                 _           _           _    _                    ")
# print("     /\         (_)         | |         | |  | |                   ")
# print("    /  \   _ __  _ ___   ___| |__   __ _| | _| | _____  _   _ _ __ ")
# print("   / /\ \ | '_ \| / __| / __| '_ \ / _` | |/ / |/ / _ \| | | | '__|")
# print("  / ____ \| | | | \__ \ \__ \ | | | (_| |   <|   < (_) | |_| | |   ")
# print(" /_/    \_\_| |_|_|___/ |___/_| |_|\__,_|_|\_\_|\_\___/ \__,_|_|   ")
# print("")
# print("")
# time.sleep(2)


def generate_launch_description():

    package_share_dir = get_package_share_directory('zion_zed_ros2_interface')
    svo_file__arg = launch.actions.DeclareLaunchArgument(name="svo_file",
                                                         default_value="",
                                                         )
    
    #include launch file
    otherFIle__include = launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PythonLaunchDescriptionSource(
                os.path.join(package_share_dir, 'launch/include/zed_camera.launch.py')
            )
        )   
    )
    
    # otherFIle__include = launch.actions.IncludeLaunchDescription(
    #     XMLLaunchDescriptionSource(os.path.join(package_share_dir, 'launch/include/zed_camera.launch.xml')
    #             )
    #         )  

    #RVIZ2 launcher
    rviz2_launcher = launch_ros.actions.Node(package='rviz2',
                                    executable='rviz2',
                                    name='Anis_rviz2_customARGS',
                                    #arguments="-d $(find zion_zed_ros2_interface)/rviz2/zed_display.rviz",
                                    #exit=launch.actions.Shutdown(),
                                    output='screen',
                                    #parameters=[{'use_sim_time': use_sim_time}])
                                )




    # Launch them all!
    return launch.LaunchDescription([
        #svo_file__arg,
        #rviz2_launcher,
        otherFIle__include,
        
    ])
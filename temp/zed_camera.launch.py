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

import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, TextSubstitution, PythonExpression
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.descriptions import ParameterValue
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution



def generate_launch_description():


    zed_wrapper_share_dir = get_package_share_directory('zed_wrapper')
    xacro_file = os.path.join(zed_wrapper_share_dir, 'urdf', 'zed_descr.urdf.xacro')

    zion_share_dir = get_package_share_directory('zion_zed_ros2_interface')
    params_path_common = os.path.join(zion_share_dir, 'params', 'common.yaml')
    params_path_zedm = os.path.join(zion_share_dir, 'params', 'zedm.yaml')

    print("Anis Used pathes")
    print(xacro_file)
    print(params_path_common)
    print(params_path_zedm)
    print("-----------------------------------------------------")
    
    package_name = "zed_wrapper"
    zed_share_dir = get_package_share_directory(package_name)
    zion_zed_share_dir = get_package_share_directory("zion_zed_ros2_interface")



    camera_name_launch_arg = launch.actions.DeclareLaunchArgument(
        "camera_name", default_value=TextSubstitution(text='zed'))

    camera_model_launch_arg = launch.actions.DeclareLaunchArgument(
        "camera_model", default_value="zed")

    node_name_launch_arg = launch.actions.DeclareLaunchArgument(
        "node_name", default_value="zed_node")
    
    svo_file_launch_arg = launch.actions.DeclareLaunchArgument(
        "svo_file", default_value="")
    
    stream_launch_arg = launch.actions.DeclareLaunchArgument(
        "stream", default_value="")
    
    base_frame_launch_arg = launch.actions.DeclareLaunchArgument(
        "base_frame", default_value="base_link")  

    publish_urdf_launch_arg = launch.actions.DeclareLaunchArgument(
        "publish_urdf", default_value='hello world')

    camera_id_launch_arg = launch.actions.DeclareLaunchArgument(
        "camera_id", default_value="0")

    gpu_id_launch_arg = launch.actions.DeclareLaunchArgument(
        "gpu_id", default_value="-1")

    cam_pos_x_launch_arg = launch.actions.DeclareLaunchArgument(
        "cam_pos_x", default_value="0.0")
    
    cam_pos_y_launch_arg = launch.actions.DeclareLaunchArgument(
        "cam_pos_y", default_value="0.0")

    cam_pos_z_launch_arg = launch.actions.DeclareLaunchArgument(
        "cam_pos_z", default_value="0.0")

    cam_roll_launch_arg = launch.actions.DeclareLaunchArgument(
        "cam_roll", default_value="0.0")

    cam_pitch_launch_arg = launch.actions.DeclareLaunchArgument(
        "cam_pitch", default_value="0.0")
    
    cam_yaw_launch_arg = DeclareLaunchArgument(
        "cam_yaw", default_value="0.0")
    
    # zed_wrapper_share_dir = get_package_share_directory('zed_wrapper')
    # xacro_file = os.path.join(zed_wrapper_share_dir, 'urdf', 'zed_descr.urdf.xacro')
    # params_path = LaunchConfiguration('params')
    # print(params_path)
    
    # print("anis1")
    # default_value_str = camera_name_launch_arg.default_value
    # print(f"camera_name:='{str(default_value_str)}'")
    # print("anis2")

    launch.actions.LogInfo(msg="Anis Logging message")
    #launch.actions.LogInfo(msg=f"xacro {xacro_file} camera_name:='{camera_name_launch_arg}'")

    # xacro_cmd = ExecuteProcess(
    #      cmd=[
    #         'xacro', 
    #         xacro_file, 
    #         'camera_name:=' +
    #         TextSubstitution(text=str(camera_name_launch_arg.default_value)),

    #         #f"xacro {xacro_file} camera_name:='{camera_name_launch_arg}'"
    # #         #f"camera_name:='{camera_name_launch_arg}'",
    # #         # f"camera_model:='{camera_model_launch_arg.default_value}'",
    # #         # f"base_frame:='{base_frame_launch_arg.default_value}'",
    # #         # f"cam_pos_x:='{cam_pos_x_launch_arg.default_value}'",
    # #         # f"cam_pos_y:='{cam_pos_y_launch_arg.default_value}'",
    # #         # f"cam_pos_z:='{cam_pos_z_launch_arg.default_value}'",
    # #         # f"cam_roll:='{cam_roll_launch_arg.default_value}'",
    # #         # f"cam_pitch:='{cam_pitch_launch_arg.default_value}'",
    # #         # f"cam_yaw:='{cam_yaw_launch_arg.default_value}'",
    #      ],
    #      shell=True,
    #      output='screen',
    #  )

# #<!-- ROS URDF description of the ZED -->
    # ros2_urdf_to_zed__launcher = launch_ros.actions.Node(
    #         package='xacro',
    #         executable='xacro',
    #         name='Anis_xacro',
    #         output='screen', #log messages and print statements, will be visible in the terminal window
    #         arguments=[
    #             f'{xacro_file}',
    #             f'camera_name:={camera_name_launch_arg.name}',
    #         ],
    #         #condition=launch.conditions.IfCondition(
    #         #            launch.substitutions.LaunchConfiguration(publish_urdf_launch_arg.default_value)),
    #     )

#     ros2_urdf_to_zed__launcher = launch_ros.actions.Node(
#             package='xacro',
#             executable='xacro',
#             name='Anis_xacro',
#             output='screen',
#             arguments=[
#                 xacro_file,
#                 f'camera_name:={camera_name_launch_arg.name}',
#                 f'camera_model:={camera_model_launch_arg.name}',
#                 f'base_frame:={base_frame_launch_arg.name}',
#                 f'cam_pos_x:={cam_pos_x_launch_arg.name}',
#                 f'cam_pos_y:={cam_pos_y_launch_arg.name}',
#                 f'cam_pos_z:={cam_pos_z_launch_arg.name}',
#                 f'cam_roll:={cam_roll_launch_arg.name}',
#                 f'cam_pitch:={cam_pitch_launch_arg.name}',
#                 f'cam_yaw:={cam_yaw_launch_arg.name}'
#             ],
#             condition=launch.conditions.IfCondition(
#                         launch.substitutions.LaunchConfiguration(publish_urdf_launch_arg.default_value)),
#         )
    

    # rsp__launcher = launch_ros.actions.Node(
    #     package='robot_state_publisher',
    #     executable='robot_state_publisher',
    #     output='screen',
    #     parameters= [{'robot_description': ParameterValue(Command(['xacro ',xacro_file,
    #                                                                'params_path:=',params_path]), value_type=str)}],
    #     #parameters=[{'use_sim_time': False}],
    #     #remappings=[('/robot_description', '/zed_description')],
    #     #condition=LaunchConfiguration("publish_urdf")

    # )

    # rsp_launcher = launch_ros.actions.Node(
    #         package='robot_state_publisher',
    #         executable='robot_state_publisher',
    #         name='Anis_rsp',
    #         output='screen',
    #         arguments=[],
    #         remappings=[('robot_description', 'zed_description')],
    #         condition=launch.conditions.IfCondition(
    #                     launch.substitutions.LaunchConfiguration(publish_urdf_launch_arg.name)),
    #     )
    

    # rsp_launcher = launch_ros.actions.Node(package='robot_state_publisher',
    #                                 executable='robot_state_publisher',
    #                                 name='Anis_zed_state_publisher',
    #                                 output='screen',
    #                                 remappings=[('/robot_description', '/zed_description'),]
    #                             )



    #RVIZ2 launcher
    # zedMINI_launcher = launch_ros.actions.Node(
    #                 package='zed_wrapper',
    #                 executable='zed_wrapper',#'zed_node',
    #                 name='Anis_zed_wrapper',
    #                 #arguments="-d $(find zion_zed_ros2_interface)/rviz2/zed_display.rviz",
    #                 #exit=launch.actions.Shutdown(),
    #                 output='screen',
    #                 parameters=
    #                 #parameters=[{'use_sim_time': use_sim_time}])
    #                 )


    #Open/Run RVIZ
    # rviz_run = launch.actions.ExecuteProcess(cmd=['rviz2'],
    #                                 name='Anis_RVIZ2_Process',
    #                                 output='screen')
    


    # Launch them all!
    return launch.LaunchDescription([
        camera_name_launch_arg,
        # camera_model_launch_arg,
        # node_name_launch_arg,
        # svo_file_launch_arg,
        # stream_launch_arg,
        # base_frame_launch_arg,
        # publish_urdf_launch_arg,
        # camera_id_launch_arg,
        # gpu_id_launch_arg,
        # cam_pos_x_launch_arg,
        # cam_pos_y_launch_arg,
        # cam_pos_z_launch_arg,
        # cam_roll_launch_arg,
        # cam_pitch_launch_arg,
        # cam_yaw_launch_arg,

        #xacro_cmd,

        #rsp__launcher,
        #rsp_launcher,
        #rviz_run,
        #zedMINI_launcher,


         Node(
            package='zed_wrapper',
            executable="zed_wrapper",
            name='Anis_zed_wrapper_node', #os.environ["node_name"],  # We use os.environ to get the value of "$(arg node_name)"
            output="screen",
            arguments=["__params:=" + params_path_common], #os.path.join(zed_share_dir, "params", "common.yaml")],
            parameters=[params_path_common, params_path_zedm],
            #     os.path.join(zed_share_dir, "params", "common.yaml"),
            #     os.path.join(zed_share_dir, "params", "zedm"), #os.environ["camera_model"] + ".yaml")
            # ]
        ),
        # Node(
        #     package="zion_zed_ros_interface",
        #     executable="camera_info_publisher_node",
        #     name="camera_info_publisher",
        #     output="screen",
        #     parameters=[{
        #         "camera_name": os.environ["camera_name"],
        #         "base_frame": os.environ["base_frame"],
        #         "svo_file": os.environ["svo_file"],
        #         "stream": os.environ["stream"],
        #         "camera_id": os.environ["camera_id"],
        #         "gpu_id": os.environ["gpu_id"]
        #     }],
        #     remappings=[
        #         ("image_raw", "camera_info_publisher/image_raw")
        #     ]
        # )

        
    ])
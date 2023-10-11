import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():

    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name = 'billee_bot'  

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
            )
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    imu = Node(package='realsense_camera', executable="imu")

    robot_localization = Node(package='robot_localization', executable='ukf_node',
                              parameters=[{'imu0': '/odom/Imu',
                                           "imu0_config": [False, False, False,
                                                           True, True, True,
                                                           False, False, False,
                                                           True, True, True,
                                                           True, True, True]}])
    
    cost_map = Node(package="nav2_costmap_2d", executable="nav2_costmap_2d", 
                    parameters=[{"file": "$(find nav2_costmap_2d)/launch/example/example_params.yaml",
                                 "command": "load", 
                                 "ns": "costmap"}])

    return LaunchDescription([
        rsp,
        imu,
        robot_localization,
        cost_map
    ])

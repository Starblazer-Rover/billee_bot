import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
<<<<<<< HEAD
    # Get the package share directory
    your_package_share_directory = get_package_share_directory('billee_bot')

    # Define the launch description
    ld = LaunchDescription()

    # Start the costmap node
    costmap_node = Node(
        package='nav2_costmap_2d',
        executable='nav2_costmap_2d',
        name='costmap_node',
        output='screen',
        parameters=[your_package_share_directory + '/config/costmap_params.yaml']
    )

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='robot_localization_node',
        output='screen',
        parameters=[{
                     'odom_frame': 'odom', 
                     'base_link_frame': 'base_link',
                     'map_frame': 'map',
                     'world_frame': 'odom',  
                     'two_d_mode': True,
                     'print_diagnostics': True,
                     'imu0': '/movement/Imu',
                     'imu0_config': [False, False, False,
                                     False, False, True,
                                     False, False, False,
                                     False, False, False,
                                     False, False, False],
                      'odom0': '/odom/Encoder', 
                      'odom0_config': [True, True, False,
                                       False, False, True, 
                                       False, False, False, 
                                       False, False, False, 
                                       False, False, False]
                    }]
    )

    """ 
    
    'imu0': '/movement/Imu',
                     'imu0_config': [False, False, False,
                                     True, True, True,
                                     False, False, False,
                                     True, True, True,
                                     True, True, True],"""

    #ld.add_action(costmap_node)
    ld.add_action(robot_localization_node)



    return ld
=======
    return LaunchDescription([
        # rtabmap node
        Node(
            package='rtabmap_launch',
            executable='rtabmap',
            name='rtabmap',
            output='screen',
            parameters=[
                {'subscribe_depth': True},
                {'subscribe_rgb': False},
                {'subscribe_rgb_info': False},
                {'frame_id': 'base_link'},
                {'odom_frame_id': 'odom'}
            ],
            remappings=[
                ('depth/image', '/map/PointCloud2'),
                ('depth/camera_info', '/custom/depth/camera_info'),
                ('odom', '/custom/odom')
            ]
        )
    ])
>>>>>>> 589ef42 (feat: 5/31/2024)

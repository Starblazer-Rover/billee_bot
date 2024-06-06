from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='realsense_camera',
            executable='camera',
        ),

        Node(
            package='realsense_camera',
            executable='depth'
        ),

        Node(
            package='realsense_camera',
            executable='image'
        ),

        Node(
            package='sensors',
            executable='camera',
            parameters=[
                {
                    'video': 6,
                    'port': 12346
                }
            ]
        ),

        Node(
            package='sensors',
            executable='camera',
            parameters=[
                {
                    'video': 8,
                    'port': 12347
                }
            ]
        ),

        Node(
            package='manual_movement',
            executable='encoder'
        ),

        Node(
            package='sensors',
            executable='imu'
        ),

        Node(
            package='odometry_frame',
            executable='odom'
        ),

        Node(
            package='odometry_frame',
            executable='transform'
        ),

        Node(
            package='sensors',
            executable='gps'
        ),

        Node(
            package='odometry_frame',
            executable='target'
        ),

        Node(
            package='map_frame',
            executable='map'
        ),

        Node(
            package='manual_movement', 
            executable='autonomous',
        ),
    ])
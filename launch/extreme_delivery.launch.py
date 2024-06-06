from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='manual_movement', 
            executable='rover_movement',
        ),

        Node(
            package='manual_movement',
            executable='arm'
        ),

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
    ])
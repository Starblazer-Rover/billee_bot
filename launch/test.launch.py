from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='sensors',
            executable='camera',
            parameters=[
                {
                    'video': 0,
                    'port': 12349
                }
            ]
        ),

        Node(
            package='sensors',
            executable='camera',
            parameters=[
                {
                    'video': 2,
                    'port': 12350
                }
            ]
        ),
    ])
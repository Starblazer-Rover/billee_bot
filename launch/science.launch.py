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
                    'video': 1,
                    'port': 12348
                }
            ]
        ),

        Node(
            package='sensors',
            executable='camera',
            parameters=[
                {
                    'video': 10,
                    'port': 12349
                }
            ]
        ),
    ])
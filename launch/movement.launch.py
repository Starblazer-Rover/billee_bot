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
            package='sensors',
            executable='camera',
            parameters=[
                {
                    'video': 4,
                    'port': 12348
                }
            ]
        ),
    ])
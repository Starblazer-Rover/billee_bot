from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():

    camera_1 = Node(
            package='realsense_camera',
            executable='client',
            parameters=[
                {
                    'topic': '/camera2',
                    'port': 12346
                }
            ]
        )
    
    camera_2 = Node(
            package='realsense_camera',
            executable='client',
            parameters=[
                {
                    'topic': '/camera3',
                    'port': 12347
                }
            ]
        )
    
    camera_3 = Node(
            package='realsense_camera',
            executable='client',
            parameters=[
                {
                    'topic': '/camera4',
                    'port': 12348
                }
            ]
        )
    
    camera_4 = Node(
            package='realsense_camera',
            executable='client',
            parameters=[
                {
                    'topic': '/camera5',
                    'port': 12349
                }
            ]
        )
    
    camera_5 = Node(
            package='realsense_camera',
            executable='client',
            parameters=[
                {
                    'topic': '/camera1',
                    'port': 12350
                }
            ]
        )

    return LaunchDescription([
        camera_1,
        camera_2,
        camera_3,
        camera_4,
        camera_5
    ])
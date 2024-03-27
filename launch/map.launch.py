from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
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
    ld.add_action(costmap_node)

    return ld

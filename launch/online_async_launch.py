import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    package_name='safari_bot' 
    world_path=os.path.join(get_package_share_directory(package_name),'worlds/my_world.sdf')
    params_file=os.path.join(get_package_share_directory(package_name),'config/mapper_params_online_sync.yaml')
    use_sim_time = LaunchConfiguration('use_sim_time')

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')
    
    start_async_slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        parameters=[params_file, {'use_sim_time': use_sim_time}],
        output='screen')



    # Launch them all!
    return LaunchDescription([
        DeclareLaunchArgument(name='world', default_value=world_path,description='world_path'),
        DeclareLaunchArgument('use_sim_time',default_value='True',description='Use sim time if true'),
        DeclareLaunchArgument(name='params_file', default_value=params_file,description='parameters for slam_toolbox_node'),
        rsp,
        gazebo,
        spawn_entity,
        start_async_slam_toolbox_node
    ])

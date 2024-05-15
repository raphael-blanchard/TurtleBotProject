import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable

def generate_launch_description():
    return LaunchDescription([
        # Set the TURTLEBOT3_MODEL environment variable
        SetEnvironmentVariable('TURTLEBOT3_MODEL', 'waffle_pi'),

        # Launch the TurtleBot3 Gazebo simulation
        ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_gazebo', 'turtlebot3_house.launch.py'],
            output='screen'
        ),

        # Run the teleop keyboard control
        ExecuteProcess(
            cmd=['ros2', 'run', 'turtlebot3_teleop', 'teleop_keyboard'],
            output='screen'
        )
    ])

import subprocess
import os

def launch_turtlebot3_gazebo():
    try:
        # Launch the TurtleBot3 Gazebo simulation
        gazebo_process = subprocess.Popen(
            ['ros2', 'launch', 'turtlebot3_gazebo', 'turtlebot3_house.launch.py']
        )
        print("TurtleBot3 Gazebo simulation launched successfully.")
        return gazebo_process
    except Exception as e:
        print(f"Failed to launch TurtleBot3 Gazebo simulation: {e}")
        return None

def run_teleop_keyboard():
    try:
        # Run the teleop keyboard control
        teleop_process = subprocess.Popen(
            ['ros2', 'run', 'turtlebot3_teleop', 'teleop_keyboard']
        )
        print("Teleop keyboard control launched successfully.")
        return teleop_process
    except Exception as e:
        print(f"Failed to launch teleop keyboard control: {e}")
        return None

if __name__ == '__main__':
    # Set the TURTLEBOT3_MODEL environment variable
    os.environ['TURTLEBOT3_MODEL'] = 'waffle_pi'  # or 'waffle' or 'waffle_pi', depending on your model

    # Launch the Gazebo simulation
    gazebo_process = launch_turtlebot3_gazebo()

    # Give Gazebo some time to start up
    if gazebo_process is not None:
        import time
        time.sleep(10)

        # Run the teleop keyboard control
        teleop_process = run_teleop_keyboard()

        # Wait for the processes to complete
        if teleop_process is not None:
            teleop_process.wait()

        # Terminate the Gazebo simulation when done
        if gazebo_process is not None:
            gazebo_process.terminate()
            gazebo_process.wait()

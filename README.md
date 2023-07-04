# ROS2 Publisher Subscriber

This repository contains code for a basic ROS2 Publisher and Subscriber program implemented in Python.

## Installation

To use this code, you need to have ROS2 installed on your system. Follow the ROS2 installation instructions from the official ROS2 documentation.

## Creating ROS2 Packages

To create a ROS2 package, follow these steps:

1. Create a new directory for your package:

```markdown
  mkdir -p ~/ros2_ws/src
  cd ~/ros2_ws/src
```

2. Initialize a new ROS2 package:

```markdown
  ros2 pkg create --build-type ament_python <Package_Name>

  Example:  ros2 pkg create --build-type ament_python pubsub_pkg
```

3. Copy the provided Python scripts (publisher.py and subscriber.py) into the 'pubsub_pkg' package directory.

4. Edit the 'setup.py' file in the 'pubsub_pkg' package directory to include the following console scripts entry points:

```markdown
  entry_points={
        'console_scripts': [
                'talker = pubsub_pkg.publisher:main',
                'listener = pubsub_pkg.subscriber:main'
        ],
},

```
5. Edit the 'package.xml' file and add the following dependencies for execution

```
  <exec_depend>rclpy</exec_depend>
  <exec_depend>std_msgs</exec_depend>
``` 
## Building and Running the Publisher and Subscriber

To build and run the publisher and subscriber nodes, follow these steps:

1. Build the ROS2 workspace:

```
  cd ~/ros2_ws
  colcon build --packages-select pubsub_pkg
```
2. Source the setup script:
```
  source install/setup.bash
```

3. Run the publisher:
```
  ros2 run pubsub_pkg talker
```

4. In a separate terminal, run the subscriber:
```
  ros2 run pubsub_pkg listener
```
Do not forget to source the terminal every time you open a new terminal


The publisher will start publishing messages, and the subscriber will receive and display the messages.

The code is tested with python 3.8 , Ubuntu 20.04 - ROS2 Foxy 

## License

This project is licensed under the [MIT License](LICENSE).

Aurthor: rupesh32003@gmail.com

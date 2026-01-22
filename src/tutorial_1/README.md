# tutorial_1 – ROS 2 Fundamentals with Turtlesim

This package introduces core ROS 2 concepts using Python (`rclpy`) and the `turtlesim` simulator.
It focuses on node creation, timed execution, topic-based communication, and closed-loop control.

---

## Concepts Covered

- ROS 2 node creation using `rclpy`
- Timers and periodic callbacks
- Publishers and subscribers
- Standard ROS 2 message types
- Topic-based communication
- Open-loop and closed-loop motion control
- Feedback-driven decision logic

---

## Nodes Implemented

### 1. Node_0 – Basic Timer Node
- Demonstrates ROS 2 node initialization
- Uses a timer callback to log messages periodically
- Introduces the ROS 2 executor and spinning

**Concepts:** Timers, logging, node lifecycle

---

### 2. Node_1__Draw_Circle – Open-Loop Motion Control
- Publishes velocity commands to `/turtle1/cmd_vel`
- Makes the turtle move in a circular trajectory
- Demonstrates continuous publishing using a timer

**Topics Used:**
- `/turtle1/cmd_vel` (`geometry_msgs/Twist`)

**Concepts:** Publishers, velocity control, open-loop motion

---

### 3. Node_2__Pose_Subscriber – Pose Feedback
- Subscribes to the turtle’s pose data
- Logs position and orientation values in real time

**Topics Used:**
- `/turtle1/pose` (`turtlesim/Pose`)

**Concepts:** Subscribers, message callbacks, sensor feedback

---

### 4. Node_3__Closed_Loop_Turtle_Controller – Boundary Control
- Subscribes to turtle pose
- Publishes velocity commands based on position feedback
- Keeps the turtle within predefined boundaries using conditional logic

**Topics Used:**
- `/turtle1/pose` (`turtlesim/Pose`)
- `/turtle1/cmd_vel` (`geometry_msgs/Twist`)

**Concepts:** Closed-loop control, feedback systems, basic decision logic

---

## How to Run

Ensure `turtlesim` is running:
```bash
ros2 run turtlesim turtlesim_node

Run individual nodes as required:

ros2 run tutorial_1 test_node
ros2 run tutorial_1 draw_circle
ros2 run tutorial_1 pose_subscriber
ros2 run tutorial_1 turtle_controller_cl

# ROS 2 Tutorials – Robo Research

This repository is a structured ROS 2 workspace containing multiple tutorial packages developed incrementally to learn and demonstrate core ROS 2 concepts using Python.

The workspace is designed to scale, with each tutorial implemented as an independent ROS 2 package.

---

## Repository Structure

ros2_tutorials_ws/
└── src/
├── tutorial_1/
└── tutorial_2/ (future)


Each package inside `src/` represents a self-contained tutorial focusing on specific ROS 2 concepts.

---

## Current Packages

### tutorial_1 – ROS 2 Fundamentals with Turtlesim
Introduces core ROS 2 concepts using the `turtlesim` simulator, including:
- Node creation using `rclpy`
- Timers and periodic callbacks
- Publishers and subscribers
- Topic-based communication
- Open-loop and closed-loop motion control
- Feedback-driven decision logic

---

## Build Instructions

From the workspace root:

```bash
colcon build
source install/setup.bash
```
Each package can then be executed independently using ros2 run.

## Purpose

This repository serves as:
- A learning workspace for ROS 2
- A reference for basic ROS 2 design patterns
- A foundation for more advanced topics such as services, actions, navigation, and robot control

Future tutorial packages will be added incrementally to expand the scope of the workspace.



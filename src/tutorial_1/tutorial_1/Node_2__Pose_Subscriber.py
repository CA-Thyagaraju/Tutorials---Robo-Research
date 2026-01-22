#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Pose_Subscriber(Node):
    def __init__(self):
        super().__init__("Pose_Subscriber")
        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.callback_fn_pose, 10)

    def callback_fn_pose(self, msg: Pose):
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args=args)
    node = Pose_Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

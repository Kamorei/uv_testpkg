#!/usr/bin/env python3

# test script to verify that pip works under uv environment with ros 2

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import moviepy
import numpy

class UVPipTestNode(Node):
    def __init__(self):
        super().__init__('uv_pip_test_node')
        self.publisher_ = self.create_publisher(String, 'uv_pip_test_topic', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'moviepy version: {moviepy.__version__}, numpy version: {numpy.__version__}, count: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    uv_pip_test_node = UVPipTestNode()
    try:
        rclpy.spin(uv_pip_test_node)
    except KeyboardInterrupt:
        pass
    finally:
        uv_pip_test_node.destroy_node()
        rclpy.shutdown()
    
if __name__ == '__main__':
    main()
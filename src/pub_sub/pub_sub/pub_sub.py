#!/usr/bin/env python3
# Copyright 2024 Robotics Content Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1, self.publish)

    def publish(self):
        msg = String()
        msg.data = 'Hello, World!'

        self.publisher.publish(msg)

class MySubscriber1(Node):
    def __init__(self):
        super().__init__('subscriber1')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

class MySubscriber2(Node):
    def __init__(self):
        super().__init__('subscriber2')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    publisher = MyPublisher()
    subscriber1 = MySubscriber1()
    subscriber2 = MySubscriber2()
    executor = SingleThreadedExecutor()
    executor.add_node(publisher)
    executor.add_node(subscriber1)
    executor.add_node(subscriber2)

    executor.spin()

if __name__ == '__main__':
    main()
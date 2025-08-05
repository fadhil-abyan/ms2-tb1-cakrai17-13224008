#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class AutonomousCmdBridge(Node):
    def __init__(self):
        super().__init__('autonomous_cmd_bridge')

        # ==============================================
        # PARAMETER DECLARATION
        # ==============================================
        self.declare_parameter('default_linear_vel', 0.5)
        self.declare_parameter('default_angular_vel', 0.5)
        self.declare_parameter('publish_rate', 10.0)

        # ==============================================
        # PARAMETER RETRIEVAL
        # ==============================================
        self.linear_vel = self.get_parameter('default_linear_vel').get_parameter_value().double_value
        self.angular_vel = self.get_parameter('default_angular_vel').get_parameter_value().double_value
        publish_rate = self.get_parameter('publish_rate').get_parameter_value().double_value

        # ==============================================
        # PUBLISHER
        # ==============================================
        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            'cmd_vel',
            10
        )

        # ==============================================
        # SUBSCRIBER
        # ==============================================
        self.cmd_subscriber = self.create_subscription(
            String,
            'autonomous_cmd',
            self.command_callback,
            10
        )

        # ==============================================
        # TIMER
        # ==============================================
        self.timer = self.create_timer(
            1.0 / publish_rate,
            self.timer_callback
        )

        self.current_command = 'stop'
        self.get_logger().info('Autonomous Command Bridge started!')

    # ==================================================
    # SUBSCRIBER CALLBACK
    # ==================================================
    def command_callback(self, msg: String):
        """Callback when receiving command from topic 'autonomous_cmd'."""
        self.current_command = msg.data.strip().lower()
        self.get_logger().info(f'Received command: {self.current_command}')

    # ==================================================
    # TIMER CALLBACK
    # ==================================================
    def timer_callback(self):
        """Sends velocity commands periodically based on the last received command."""
        twist = Twist()

        if self.current_command == 'forward':
            twist.linear.x = self.linear_vel
        elif self.current_command == 'backward':
            twist.linear.x = -self.linear_vel
        elif self.current_command == 'left':
            twist.angular.z = self.angular_vel
        elif self.current_command == 'right':
            twist.angular.z = -self.angular_vel
        elif self.current_command == 'stop':
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        else:
            self.get_logger().warn(f'Unknown command: {self.current_command}')
            return

        self.cmd_vel_publisher.publish(twist)
        self.get_logger().debug(f'Published Twist: linear={twist.linear.x}, angular={twist.angular.z}')


def main(args=None):
    rclpy.init(args=args)
    node = AutonomousCmdBridge()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
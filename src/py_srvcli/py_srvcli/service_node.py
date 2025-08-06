#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from example_interfaces.srv import Trigger
from cv_bridge import CvBridge
import cv2
import os
from datetime import datetime


class ImageSaverService(Node):
    def __init__(self):
        super().__init__('image_saver_service')

        # Subscribe to image topic
        self.subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',  # Change topic name if needed
            self.image_callback,
            10
        )

        # Create service
        self.srv = self.create_service(Trigger, 'save_image', self.save_image_callback)

        self.bridge = CvBridge()
        self.latest_image = None

        self.get_logger().info("Image saver service started. Waiting for service calls...")

    def image_callback(self, msg):
        """Callback for incoming images."""
        self.latest_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    def save_image_callback(self, request, response):
        """Service callback to save the latest image."""
        if self.latest_image is None:
            response.success = False
            response.message = "No image received yet."
            return response

        # Ensure 'images' folder exists
        save_dir = os.path.join(os.getcwd(), "images")
        os.makedirs(save_dir, exist_ok=True)

        # Save image with timestamp inside 'images' folder
        filename = datetime.now().strftime("image_%Y%m%d_%H%M%S.jpg")
        save_path = os.path.join(save_dir, filename)
        cv2.imwrite(save_path, self.latest_image)

        response.success = True
        response.message = f"Image saved to {save_path}"
        self.get_logger().info(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ImageSaverService()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

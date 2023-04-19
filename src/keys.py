#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

# ROS node initialization
rospy.init_node("Keys")
pub = rospy.Publisher("keys_cmd", Twist, queue_size=10)
rate = rospy.Rate(10)

# Define key mappings
key_mappings = {
    pygame.K_UP: 0.1,
    pygame.K_DOWN: -0.1,
}

def send_cmd_vel(key):
    cmd_vel = Twist()
    if key in key_mappings:
        cmd_vel.linear.x = key_mappings[key]
    return cmd_vel

if __name__ == "__main__":
    try:
        while not rospy.is_shutdown():
          pub.publish(cmd)
          rate.sleep()
    except rospy.ROSInterruptException:
        pass

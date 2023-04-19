#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(data):
    rospy.loginfo("Linear Velocity: %s", data.linear.x)

def listener():
    rospy.init_node("test_keys_cmd_listener")
    rospy.Subscriber("keys_cmd", Twist, cmd_vel_callback)
    rospy.spin()

if __name__ == "__main__":
    listener()

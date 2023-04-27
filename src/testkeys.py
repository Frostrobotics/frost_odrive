#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(msgs):
    # rospy.loginfo("Linear Velocity: %s", data.linear.x)
    print(msgs.data)

def listener():
    rospy.init_node("test_keys_cmd_listener")
    rospy.Subscriber("cmd_vel", Twist, cmd_vel_callback)

    rospy.spin()

if __name__ == "__main__":
    listener()

#!/usr/bin/env python
import rospy
import keyboard
from geometry_msgs.msg import Twist



# Define key mappings
key_mappings = {
    "up": 0.1,
    "down": -0.1,
}

def send_cmd_vel(key):
    cmd_vel = Twist()
    if key in key_mappings:
        cmd_vel.linear.x = key_mappings[key]
    return cmd_vel



if __name__=="__main__":
    # ROS node initialization
    rospy.init_node("Keys")
    pub = rospy.Publisher("keys_cmd", Twist, queue_size=10)
    rate = rospy.Rate(10)

    while(true):
        event=keyboard.read_event()
        pub.publish(send_cmd_vel(event.name.lower()))
        rate.sleep() 
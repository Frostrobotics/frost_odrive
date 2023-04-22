#!/usr/bin/env python
# import rospy
import keyboard
import tty, sys, termios
if sys.platform == 'win32':
    import msvcrt
from select import select
# from geometry_msgs.msg import Twist



# Define key mappingsblank
key_mappings = {
    "w": 0.1,
    "s": -0.1,
    "a": 0.0
}

def getKeyPress():
    settings = None
    if sys.platform == 'win32':
        key = msvcrt.getwch()
        settings = None
    else:
        settings = termios.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select([sys.stdin], [], [], 10)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    
    print(key)
    return key
    

def send_cmd_vel(key):
#     cmd_vel = Twist()
    cmd = None
    if key in key_mappings:
        # cmd_vel.linear.x = key_mappings[key]
        cmd = key_mappings[key]
    # return cmd_vel
    print(cmd)



if __name__=="__main__":
    # ROS node initialization
    rospy.init_node("Keys")
    pub = rospy.Publisher("keys_cmd", Twist, queue_size=10)
    rate = rospy.Rate(100)
    while True:
        keys = getKeyPress()
        send_cmd_vel(keys)

    # while(true):
    #     event=keyboard.read_event()
    #     pub.publish(send_cmd_vel(event.name.lower()))
    #     rate.sleep() 
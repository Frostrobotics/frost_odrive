#!/usr/bin/env python
import rospy
import tty, sys, termios
if sys.platform == 'win32':
    import msvcrt
from select import select
from geometry_msgs.msg import Twist



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
    
    # print(key)
    return key
    

def send_cmd_vel():
    rospy.init_node("Keys")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
    rate = rospy.Rate(100) # 10Hz

    t = Twist()
    cmd = None

    while not rospy.is_shutdown():
        key = getKeyPress()
        if key in key_mappings:
            # cmd_vel.linear.x = key_mappings[key]
            cmd = key_mappings[key]
            t.linear.x = cmd
            rospy.loginfo(t)
            # print("THIS IS PUBLISHING: ", cmd)
            pub.publish(t)
        else:
            print("That key is not mapped to anything!")



if __name__=="__main__":

    # ROS node initialization
    # rospy.init_node("Keys")
    # pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
    # rate = rospy.Rate(100)

    # keys = getKeyPress()
    try:
        send_cmd_vel()
    except rospy.ROSInterruptException:
        print("WE HAVE AN ERROR")
        pass

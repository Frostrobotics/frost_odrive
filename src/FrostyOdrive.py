#!/usr/bin/env python3

import odrive_interface
import rospy

FrostO = odrive_interface.frostyOdrive()
velocity = 0

def runOdrive(msgs):
    print(msgs)
    velocity += msgs.data

    FrostO.runMotor(velocity)

def getVelocity(msgs):
    rospy.init_node("ODrive")
    rospy.Subscriber("cmd_vel", runOdrive)

    rospy.spin()

if __name__ == "__main__":
    getVelocity()
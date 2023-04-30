#!/usr/bin/env python3

import odrive_interface
import rospy

FrostO = odrive_interface.frostyOdrive()

def sendVelocity(msgs):
    
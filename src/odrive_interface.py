#!/usr/bin/env python3

import odrive
from odrive.enums import *
from odrive import *
import logging
import time
import rospy
import math

class frostyOdrive:
    def __init__(self):
        self.driver = None
        self.motor1 = None
        self.calibration = False
    

    def connectOdrive(self):
        if(self.driver != None):
            print("Odrive is already connected")
        else:
            print("Odrive is not connected, we will try to connect to one")
            try:
                self.driver = odrive.find_any(timeout=15) # timeout is default and so is the logger
                self.motor1 = self.driver.axis1
                print("Odrive is connected!!")
            except:
                print("Error cannot find odrive")
    
    def teleOpDriveMotors(self, velo, omega, base, radius):
        angular_left = (velo - (omega *(base/2)))/radius
        angular_right = (velo + (omega *(base/2)))/radius

        # set the velocity control mode
        self.motor1.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
        self.motor1.controller.input_vel = angular_right # this is the right motor
    
    def testDriveMotor(self):
        print("starting the motors!!!!")
        print("----------------------- Make sure hands and wires are out of the motors -----------------------------")
        self.motor1.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
        self.motor1.controller.input_vel = 5


    def runCalibration(self):
        if self.calibration == False and self.motor1 != None:
            logging.warning("Don't touch the robot calibrating motor")
            self.motor1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
            time.sleep(1)
            
            self.calibration = True

            return True
        else:
            logging.warning("Motor Already calibrated theres no need")
    
    def runMotor(self, velocity):
        # if self.calibration:
        self.motor1.controller.input_vel = velocity
            # time.sleep(10)
            # self.motor1.controller.input_vel = 0
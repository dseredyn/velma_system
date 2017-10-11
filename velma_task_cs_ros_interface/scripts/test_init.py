#!/usr/bin/env python
import roslib; roslib.load_manifest('velma_task_cs_ros_interface')

import rospy
import PyKDL

from velma_common.velma_interface import *

def exitError(code):
    if code == 0:
        print "OK"
        exit(0)
    print "ERROR:", code
    exit(code)

if __name__ == "__main__":

    rospy.init_node('test_init', anonymous=True)

    rospy.sleep(1)

    print "This test/tutorial executes initialization"\
        " procedures required for robot operation.\n"

    print "Running python interface for Velma..."
    velma = VelmaInterface("/velma_task_cs_ros_interface")
    print "Waiting for VelmaInterface initialization..."
    if not velma.waitForInit(timeout_s=10.0):
        print "Could not initialize VelmaInterface\n"
        exitError(1)
    print "Initialization ok!\n"

    print "Motors must be enabled every time after the robot enters safe state."
    print "If the motors are already enabled, enabling them has no effect."
    print "Enabling motors..."
    if velma.enableMotors() != 0:
        exitError(14)

    print "Also, head motors must be homed after start-up of the robot."
    print "Sending head pan motor START_HOMING command..."
    velma.startHomingHP()
    if velma.waitForHP() != 0:
        exitError(14)
    print "Head pan motor homing successful."

    print "Sending head tilt motor START_HOMING command..."
    velma.startHomingHT()
    if velma.waitForHT() != 0:
        exitError(15)
    print "Head tilt motor homing successful."

    exitError(0)

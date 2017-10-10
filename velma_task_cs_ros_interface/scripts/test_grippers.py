#!/usr/bin/env python
import roslib; roslib.load_manifest('velma_task_cs_ros_interface')
import rospy
import math
from velma_common.velma_interface import *

def exitError(code):
    if code == 0:
        print "OK"
        exit(0)
    print "ERROR:", code
    exit(code)

if __name__ == "__main__":

    rospy.init_node('grippers_test', anonymous=True)

    rospy.sleep(1)

    velma = VelmaInterface("/velma_task_cs_ros_interface")
    print "waiting for init..."

    if not velma.waitForInit(timeout_s=20):
        print "could not initialize VelmaInterface"
        exitError(1)
    print "init ok"

    if velma.enableMotors() != 0:
        exitError(14)

    print "sending head pan START_HOMING command"
    velma.startHomingHP()
    if velma.waitForHP() != 0:
        exitError(14)

    print "sending head tilt START_HOMING command"
    velma.startHomingHT()
    if velma.waitForHT() != 0:
        exitError(15)

    print "reset left"
    velma.resetHandLeft()
    if velma.waitForHandLeft() != 0:
        exitError(2)
    rospy.sleep(0.5)
    if not isHandConfigurationClose( velma.getHandLeftCurrentConfiguration(), [0,0,0,0]):
        exitError(3)

    print "reset right"
    velma.resetHandRight()
    if velma.waitForHandRight() != 0:
        exitError(4)
    rospy.sleep(0.5)
    if not isHandConfigurationClose( velma.getHandRightCurrentConfiguration(), [0,0,0,0]):
        exitError(5)

    dest_q = [90.0/180.0*math.pi,0,0,0]
    print "move left:", dest_q
    velma.moveHandLeft(dest_q, [1,1,1,1], [2000,2000,2000,2000], 1000, hold=True)
    if velma.waitForHandLeft() != 0:
        exitError(6)
    rospy.sleep(0.5)
    if not isHandConfigurationClose( velma.getHandLeftCurrentConfiguration(), dest_q):
        print velma.getHandLeftCurrentConfiguration(), dest_q
        exitError(7)

    dest_q = [90.0/180.0*math.pi,0,0,0]
    print "move right:", dest_q
    velma.moveHandRight(dest_q, [1,1,1,1], [2000,2000,2000,2000], 1000, hold=True)
    if velma.waitForHandRight() != 0:
        exitError(8)
    rospy.sleep(0.5)
    if not isHandConfigurationClose( velma.getHandRightCurrentConfiguration(), dest_q):
        exitError(9)

    dest_q = [0,90.0/180.0*math.pi,0,180.0/180.0*math.pi]
    print "move right:", dest_q
    velma.moveHandRight(dest_q, [1,1,1,1], [2000,2000,2000,2000], 1000, hold=True)
    if velma.waitForHandRight() != 0:
        exitError(10)
    rospy.sleep(0.5)
    if not isHandConfigurationClose( velma.getHandRightCurrentConfiguration(), dest_q):
        exitError(11)

    print "reset left"
    velma.resetHandLeft()
    if velma.waitForHandLeft() != 0:
        exitError(12)
    rospy.sleep(0.5)
    if not isHandConfigurationClose( velma.getHandLeftCurrentConfiguration(), [0,0,0,0]):
        exitError(13)

    print "reset right"
    velma.resetHandRight()
    if velma.waitForHandRight() != 0:
        exitError(14)
    rospy.sleep(0.5)
    if not isHandConfigurationClose( velma.getHandRightCurrentConfiguration(), [0,0,0,0]):
        exitError(15)

    exitError(0)


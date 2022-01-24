#region VEXcode Generated Robot Configuration
import math
import random
from vexcode import *

drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()

#endregion VEXcode Generated Robot Configuration
# Library imports
from vexcode import *
from math import *
from random import randint


drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()

def driveXDistance(setpoint,duration):
    brain.timer_reset()
    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        brain.print(currentXLocation)
        brain.new_line()
        if( currentXLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentXLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
   
        wait(1,MSEC)
    drivetrain.stop()


def driveYDistance(setpoint,duration):
    brain.timer_reset()
    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        if( currentYLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
 
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagDistance(setpoint,duration):
    brain.timer_reset()

    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        if( currentXLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentXLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
        
        wait(1,MSEC)
    drivetrain.stop()


def main():
    pen.move(DOWN)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    driveXDistance(0,5)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,5)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagDistance(398,4)

# VR threads — Do not delete
vr_thread(main())

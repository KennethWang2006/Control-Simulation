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
    TOLERANCE = 0
    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        k = 1
        speed = k*error
        drivetrain.set_drive_velocity(speed,PERCENT)
        brain.print(currentXLocation)
        brain.new_line()
        if( currentXLocation < setpoint - TOLERANCE):
            drivetrain.drive(FORWARD)
        elif (currentXLocation > setpoint + TOLERANCE):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
   
        wait(1,MSEC)
    drivetrain.stop()


def driveYDistance(setpoint,duration):
    brain.timer_reset()
    TOLERANCE = 0
    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        error = setpoint - currentYLocation
        k = 1
        speed = k*error
        drivetrain.set_drive_velocity(speed,PERCENT)
        if( currentYLocation < setpoint - TOLERANCE):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint + TOLERANCE):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
 
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagDistance(setpoint,duration):
    brain.timer_reset()
    TOLERANCE = 0
    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        k = 1
        speed = k*error
        drivetrain.set_drive_velocity(speed,PERCENT)
        if( currentXLocation < setpoint - TOLERANCE):
            drivetrain.drive(FORWARD)
        elif (currentXLocation > setpoint + TOLERANCE):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
        
        wait(1,MSEC)
    drivetrain.stop()


def main():
    pen.move(DOWN)
    drivetrain.turn_for(RIGHT, 90, DEGREES,wait=True)
    driveXDistance(0,3)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,3)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagDistance(398,4)

# VR threads — Do not delete
vr_thread(main())

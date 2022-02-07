import board
import busio
import time
import math

from sphero_rvr import *

import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D10)

rvr = RVRDrive()
rvr.wake()
rvr.set_all_leds(255,0,0)
time.sleep(0.1)
rvr.set_all_leds(0,255,0)
time.sleep(0.1)
rvr.set_all_leds(0,0,255)
time.sleep(0.1)
rvr.set_all_leds(0,0,0)

#Set control parameters
setpoint = 100.0
k = 3
MAX_SPEED = 100

while True:
    try:
        sensor_distance = sonar.distance

        # Add your proportional control code here.

        if(output > MAX_SPEED):
            output = MAX_SPEED
        elif(output < -MAX_SPEED):
            output = -MAX_SPEED

        # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
        # Use this command in the next line to send the output of your proportional
        # control to both the left and right motors.

    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.2)

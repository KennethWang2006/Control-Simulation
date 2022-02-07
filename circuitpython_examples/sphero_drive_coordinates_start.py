

import board
import busio
import time
import math

from sphero_rvr import *


rvr = RVRDrive()
rvr.wake()
rvr.set_all_leds(255,0,0)
time.sleep(0.1)
rvr.set_all_leds(0,255,0)
time.sleep(0.1)
rvr.set_all_leds(0,0,255)
time.sleep(0.1)
rvr.set_all_leds(0,0,0)

time.sleep(1.0)
SPEED = 0.5
PI_OVER_3 = 3.14159/3

# API Usage:
# drive_to_position_si(PI_OVER_3,1.5,1,SPEED) will drive to the point (1.5, 1) at a speed SPEED
# and then rotate to an angle of PI_OVER_3 (60 degrees).

# Write your code here to get the RVR to move in an equilateral triangle of 1 meters per side.

time.sleep(3.0) # Wait three seconds after each drive command before sending the next one.

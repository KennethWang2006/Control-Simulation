#SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#SPDX-License-Identifier: MIT
 
 import time
 import board
 import adafruit_bno055
 
 
 i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

 #If you are going to use UART uncomment these lines
# uart = board.UART()
# sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF


def temperature():
    global last_val  # pylint: disable=global-statement
    result = sensor.temperature
    if abs(result - last_val) == 128:
        result = sensor.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result


while True:
   print("Temperature: {} degrees C".format(sensor.temperature))
  
  # the temperature sensor prints the temperature in degrees celcius
    """
   print(
        "Temperature: {} degrees C".format(temperature())
   )  # Uncomment if using a Raspberry Pi
    """
   print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
   
   # the acceleration sensor prints the acceleration in m/s^2 (meter per second squared)
   
   print("Magnetometer (microteslas): {}".format(sensor.magnetic))
   
   # the magnetic sensor prints the magnetic flux density which is equal to (10^-6 tesla)
   
   print("Gyroscope (rad/sec): {}".format(sensor.gyro))
   print("Euler angle: {}".format(sensor.euler))
   print("Quaternion: {}".format(sensor.quaternion))
   print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
   print("Gravity (m/s^2): {}".format(sensor.gravity))
   
   # the gravity sensor prints the gravitational acceleration in m/s^2 or (meter per second squared)
   
   print()
   
   time.sleep(1)

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
def rotate(deg):
    left_motor.run(360)
    time.sleep(deg/90)
    left_motor.stop()

def drive(sec):
    left_motor.run(360)
    right_motor.run(360)
    time.sleep(sec)
    left_motor.stop()
    right_motor.stop()

for i in range(4):
    drive(2)
    time.sleep(0.2)
    rotate(90)
    time.sleep(0.2)
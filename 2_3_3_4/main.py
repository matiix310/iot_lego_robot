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
CSensor = ColorSensor(Port.S2)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

speed = 100
turn_count = 0
turn = 1
turn_mul = 3

while CSensor.color() != Color.RED:
    cs = CSensor.color()

    if cs == Color.BLACK:
        speed = 100
        turn_count = 0
        robot.drive(speed, 0)
    elif cs == Color.BLUE:
        speed = 50
        turn_count = 0
        robot.drive(speed, 0)
    else:
        if turn_count >= 15:
            turn = -turn
            robot.turn(turn_count * turn * turn_mul)
            turn_count = 0
        robot.stop()
        robot.turn(turn * turn_mul)
        turn_count += 1

    ev3.screen.print(cs)
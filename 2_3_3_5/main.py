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
TSensor = TouchSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

detected_colors = [Color.RED, Color.YELLOW, Color.BLUE]
encourted_colors = []
counters = [ 0 for i in range(len(detected_colors)) ]

start = time.time()

def play_tone(cs):
    c = ""

    if cs == Color.RED:
        c = "C"
    elif cs == Color.GREEN:
        c = "D"
    elif cs == Color.YELLOW:
        c = "A"
    elif cs == Color.WHITE:
        c = "B"
    elif cs == Color.BLUE:
        c = "E"
    elif cs == Color.BLACK:
        c = "F"

    if c != "":
        ev3.speaker.play_notes([c + "4/4"])

robot.drive(50, 0)
last_color = None
while not TSensor.pressed():
    cs = CSensor.color()
    print(cs)

    if last_color != cs and cs in detected_colors:
        encourted_colors.append(cs)
        counters[detected_colors.index(cs)] += 1
        ev3.screen.print(cs, ":", counters[detected_colors.index(cs)])
    last_color = cs

# button is pressed
robot.stop()
for color in encourted_colors:
    play_tone(color)
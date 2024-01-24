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
ev3.screen.print("Bonjour")

start = time.time()

while time.time() - start < 30:
    buttonspressed = ev3.buttons.pressed()
    if (len(buttonspressed) > 0):
        c = ""
        b = buttonspressed[0]
        if b == Button.RIGHT:
            c = "D"
        elif b == Button.UP:
            c = "A"
        elif b == Button.DOWN:
            c = "B"
        elif b == Button.LEFT:
            c = "E"
        elif b == Button.CENTER:
            c = "F"
        else:
            c = "G"

        if c != "G":
            ev3.speaker.play_notes([c + "4/4"])
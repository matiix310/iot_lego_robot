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
    if (len(buttonspressed) > 0 and buttonspressed[0] == Button.CENTER):
        ev3.light.on(Color.RED)
    else:
        ev3.light.on(Color.GREEN)
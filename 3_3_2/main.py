#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
#import library
from umqtt.robust import MQTTClient
import time


# The program is for robot A equiped with a specific item to collect little lego cube and transport it


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#MQTT setup
MQTT_ClientID = 'robotA'
MQTT_Broker = '192.168.49.231'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)




# Create your objects here.
ev3 = EV3Brick()

#callback for listen to topics
def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))

# Write your program here.
client.connect()
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
CSensor = ColorSensor(Port.S2)

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
pelle = Motor(Port.D)
UltraSensor = UltrasonicSensor(Port.S4)




pelle = Motor(Port.D)



robot.drive(100, 0)
while UltraSensor.distance() > 40:
    continue
robot.stop()
pelle.run_angle(90, 130)


time.sleep(0.2)

robot.drive(100, 0)
while UltraSensor.distance() > 100:
    continue
robot.stop()
ev3.speaker.play_notes(["F2/4", "F2/4"])
client.publish(MQTT_Topic_Status, "BOUGE TOI DE LA")
time.sleep(3)
robot.straight(350)
pelle.run_angle(-90, 130)
robot.straight(-100)
robot.turn(180)
client.publish(MQTT_Topic_Status, "REVIENS C BON SALE ESCLAVE")
robot.drive(170, 0)
color = CSensor.color()
while CSensor.color() == color:
    continue
robot.stop()
robot.straight(-80)
robot.turn(180)

time.sleep(3)

robot.drive(100, 0)
while UltraSensor.distance() > 150:
    continue
robot.stop()
ev3.speaker.play_notes(["F2/4", "F2/4"])
client.publish(MQTT_Topic_Status, "BOUGE TOI DE LA")
time.sleep(3)

robot.drive(100, 0)
while UltraSensor.distance() > 40:
    continue
robot.stop()
pelle.run_angle(90, 130)


time.sleep(0.2)


robot.straight(-100)
robot.turn(180)
client.publish(MQTT_Topic_Status, "REVIENS C BON SALE ESCLAVE")
robot.drive(170, 0)
color = CSensor.color()
while CSensor.color() == color:
    continue
robot.stop()
pelle.run_angle(-90, 130)
robot.straight(-80)
robot.turn(180)





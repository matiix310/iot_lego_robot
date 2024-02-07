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

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#MQTT setup
MQTT_ClientID = "RobotA"
MQTT_Broker = '192.168.49.231'
MQTT_Topic_Status = 'Lego/Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)




# Create your objects here.
ev3 = EV3Brick()

# Motor
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

Arm = Motor(Port.D)

UltraSensor = UltrasonicSensor(Port.S4)

CSensor = ColorSensor(Port.S2)

#callback for listen to topics
def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        m = str(msg.decode())
        if (m[0] == "B"):
            ev3.screen.print(m[1:])

# Write your program here.
client.connect()
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)

distance_drive = []

robot.drive(200, 0)
robot.reset()

maintenance = 3

while maintenance > 0:
    if UltraSensor.distance() < 200:
        distance_drive.append(robot.distance())
        robot.stop()
        time.sleep(0.3)
        robot.turn(90)
        time.sleep(0.3)
        robot.drive(200, 0)
        robot.reset()
        maintenance -= 1

robot.stop()

for distance in distance_drive:
    client.publish(MQTT_Topic_Status, "AS" + str(distance))
    client.publish(MQTT_Topic_Status, "AT90")
client.publish(MQTT_Topic_Status, "AF")

time.sleep(2)

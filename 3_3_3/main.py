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

robotname = "B"

#MQTT setup
MQTT_ClientID = robotname
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
def listenB(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        m = str(msg.decode())
        if m == "Center button":
            robot.stop()
        elif m == "Left button":
            robot.turn(-90)
        elif m == "Right button":
            robot.turn(90)
        elif m == "Down button":
            robot.drive(-100, 0)
        elif m == "Up button":
            robot.drive(100, 0)

#callback for listen to topics
def listenA(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        m = str(msg.decode())
        if (m[0] == "B"):
            ev3.screen.print(m[1:])

# Write your program here.
client.connect()
if robotname == "A":
    client.set_callback(listenA)
else:
    client.set_callback(listenB)
client.subscribe(MQTT_Topic_Status)



if robotname == "A":
    active = None
    while True:
        buttonspressed = ev3.buttons.pressed()
        if (len(buttonspressed) > 0 and active != buttonspressed[0]):
            active = buttonspressed[0]
            if buttonspressed[0] == Button.CENTER:
                client.publish(MQTT_Topic_Status, "Center button")
            elif buttonspressed[0] == Button.UP:
                client.publish(MQTT_Topic_Status, "Up button")
            elif buttonspressed[0] == Button.DOWN:
                client.publish(MQTT_Topic_Status, "Down button")
            elif buttonspressed[0] == Button.RIGHT:
                client.publish(MQTT_Topic_Status, "Right button")
            elif buttonspressed[0] == Button.LEFT:
                client.publish(MQTT_Topic_Status, "Left button")
        elif (len(buttonspressed) == 0):
            active = None
        client.check_msg()
        
else:
    start = time.time()
    while True:
        client.check_msg()
        if time.time() - start > 1:
            client.publish(MQTT_Topic_Status, "B" + str(UltraSensor.distance()))
            start = time.time()

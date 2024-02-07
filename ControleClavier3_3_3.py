# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = '192.168.49.231'
port = 1883
topic = "Lego/Status"
client_id = 'Macbook'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, msg):
   
    result = client.publish(topic, msg)
    
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
        


def run():
    client = connect_mqtt()
    client.loop_start()
    start = time.time()
    while time.time() - start < 60:
        touche = input()
        if touche == "z":
            client.publish(topic, "Up button")
        elif touche == " ":
            client.publish(topic, "Center button")
        elif touche == "q":
            client.publish(topic, "Left button")
        elif touche == "s":
            client.publish(topic, "Down button")
        elif touche == "d":
            client.publish(topic, "Right button")
    
    client.loop_stop()


if __name__ == '__main__':
    run()


        

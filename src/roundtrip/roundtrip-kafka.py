import paho.mqtt.client as mqtt
from confluent_kafka import Producer
import time

start_ms = None

#kafka
conf = {
    "bootstrap.servers": "localhost:19092" ,
    "security.protocol": "PLAINTEXT",
    }
p = Producer(**conf)

def on_connect(mqtt_client, obj, flags, rc):
    mqtt_client.subscribe("otto-out")

def on_message(mqtt_client, obj, msg):
    global start_ms
    end_ms = time.time()
    print("kafka round trip time: ", (end_ms-start_ms)*1000, "ms")

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set('Flask', 'DefaultFlask')
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("localhost")

#medir roundtrip time kafka
start_ms = time.time()
p.produce("otto", b"kafka test payload")

mqtt_client.loop_forever()

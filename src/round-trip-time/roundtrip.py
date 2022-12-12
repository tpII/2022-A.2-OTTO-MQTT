import paho.mqtt.client as mqtt
from confluent_kafka import Producer
import time

start_ms = None

def on_connect(mqtt_client, obj, flags, rc):
    global start_ms
    mqtt_client.publish('debug','testing rtt!')
    mqtt_client.subscribe("otto-out")
    start_ms = time.time()
    mqtt_client.publish('otto','my test payload')

def on_message(mqtt_client, obj, msg):
    end_ms = time.time()
    print("mqtt round trip time: ", (end_ms-start_ms), "ms")

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set('Flask', 'DefaultFlask')
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("localhost")
mqtt_client.loop_forever()

# #kafka
# conf = {
#     "bootstrap.servers": "localhost:9092" ,
#     "security.protocol": "PLAINTEXT",
#     }
# p = Producer(**conf)

# #medir roundtrip time kafka
# start_time = time.time()

# producer.produce("otto", b"kafka test payload")

# while (not msg):
#     continue
# msg = False

# end_time = time.time()

# #obtener round-trip time en ms
# rt_time = (end_time - start_time) * 1000

# print("Round trip time de broker kafka: ", rt_time, "ms\n")

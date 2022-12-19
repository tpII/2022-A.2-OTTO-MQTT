import os
import paho.mqtt.client as mqtt
from confluent_kafka import Consumer

def on_connect(client, userdata, flags, rc):
    client.publish('debug',"Proxy conectado!")

if __name__ == '__main__':
    #cliente mqtt
    client = mqtt.Client()
    client.username_pw_set(os.environ['MQTT_USERNAME'], os.environ['MQTT_PASSWORD'])
    client.on_connect = on_connect
    client.connect("172.18.0.2")
    client.loop_start()

    #consumidor kafka
    conf = {
        'bootstrap.servers': '172.18.0.26:9092' ,
        'security.protocol': 'PLAINTEXT',
        'session.timeout.ms': 6000,
        'group.id': 'grupo',
        'auto.offset.reset': 'latest',
        'enable.auto.offset.store': False
        }
    c = Consumer(**conf)
    topics = ['otto']
    c.subscribe(topics)
    #c.assign(1)

    while True:
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        else:
            client.publish('otto', msg.value())
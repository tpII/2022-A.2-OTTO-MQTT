from flask import Flask
from redis import Redis
import os
import paho.mqtt.client as mqtt
from confluent_kafka import Producer
from flask import render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
redis = Redis(host="redis",port=6379)
topic = os.environ['TOPIC']

def on_connect(client, userdata, flags, rc):
    client.publish(topic, "Cliente conectado. -Flask")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/walkForward", methods=["GET", "POST"])
def walkForward():
   client.publish(topic,"walk forward")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/walkBackward", methods=["GET", "POST"])
def walkBackward():
   client.publish(topic,"walk backward")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/walkRight", methods=["GET", "POST"])
def walkRight():
   client.publish(topic,"walk right")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/walkLeft", methods=["GET", "POST"])
def walkLeft():
   client.publish(topic,"walk left")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/dance", methods=["GET", "POST"])
def dance():
   client.publish(topic,"dance")
   # (topic, msg in bytes)
   producer.produce(topic, b"hola")
   return (""), 204


if __name__ == "__main__":
   #cliente mqtt setup
   client = mqtt.Client()
   client.username_pw_set("Flask", "DefaultFlask")
   client.on_connect = on_connect
   client.connect("172.18.0.2")
   client.loop_start()

   #productor kafka setup
   conf = {
      'bootstrap.servers': os.environ['KAFKA_BROKER'],
      'session.timeout.ms': 6000,
      'default.topic.config': {'auto.offset.reset': 'smallest'},
      'security.protocol': 'SASL_SSL',
      'sasl.mechanisms': 'SCRAM-SHA-256',
      'sasl.username': os.environ['KAFKA_USERNAME'],
      'sasl.password': os.environ['KAFKA_PASSWORD']
      }

   producer = Producer(**conf)
   app.run(host="0.0.0.0", port=5000, debug=True)
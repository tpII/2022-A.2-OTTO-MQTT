from flask import Flask, render_template, flash
from redis import Redis
import os
import paho.mqtt.client as mqtt
from confluent_kafka import Producer

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
redis = Redis(host="redis",port=6379)
topic = 'otto'

def on_connect(client, userdata, flags, rc):
    client.publish(topic, "Cliente conectado. -Flask")

@app.route("/")
def home():
    flash("Actualmente te comunicas a traves de Mosquitto con Otto!")
    return render_template('home.html')

@app.route("/kafka", methods=['GET', 'POST'])
def kafka():
   flash("Excelente eleccion, ahora te comunicas a traves de Kafka con Otto!")
   client.publish(topic,"cambiame a kafka")
   producer.produce(topic, b"cambiame a kafka")
   return render_template('home-kafka.html')

@app.route("/mosquitto", methods=['GET', 'POST'])
def mosquitto():
   flash("Excelente eleccion, ahora te comunicas a traves de Mosquitto con Otto!")
   client.publish(topic,"cambiame a mosquitto")
   producer.produce(topic, b"cambiame a mosquitto")
   return render_template('home.html')


@app.route("/posInicial", methods=['GET', 'POST'])
def posInicial():
   client.publish(topic,"00")
   producer.produce(topic, b"00")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/walkForward", methods=['GET', 'POST'])
def walkForward():
   client.publish(topic,"01")
   producer.produce(topic, b"01")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/walkBackward", methods=["GET", "POST"])
def walkBackward():
   client.publish(topic,"02")
   producer.produce(topic, b"02")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/turnRight", methods=['GET', 'POST'])
def turnRight():
   client.publish(topic,"03")
   producer.produce(topic, b"03")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/turnLeft", methods=['GET', 'POST'])
def turnLeft():
   client.publish(topic,"04")
   producer.produce(topic, b"04")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/bend", methods=['GET', 'POST'])
def bend():
   client.publish(topic,"05")
   producer.produce(topic, b"05")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/shakeLeg", methods=['GET', 'POST'])
def shakeLeg():
   client.publish(topic,"06")
   producer.produce(topic, b"06")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/moonwalker", methods=['GET', 'POST'])
def moonwalker():
   client.publish(topic,"07")
   producer.produce(topic, b"07")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/crusaito", methods=['GET', 'POST'])
def crusaito():
   client.publish(topic,"08")
   producer.produce(topic, b"08")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/flapping", methods=['GET', 'POST'])
def flapping():
   client.publish(topic,"09")
   producer.produce(topic, b"09")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/swing", methods=['GET', 'POST'])
def swing():
   client.publish(topic,"10")
   producer.produce(topic, b"10")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/tiptoeSwing", methods=['GET', 'POST'])
def tiptoeSwing():
   client.publish(topic,"11")
   producer.produce(topic, b"11")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/upDown", methods=['GET', 'POST'])
def upDown():
   client.publish(topic,"12")
   producer.produce(topic, b"12")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/happy", methods=['GET', 'POST'])
def happy():
   client.publish(topic,"13")
   producer.produce(topic, b"13")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/sad", methods=['GET', 'POST'])
def sad():
   client.publish(topic,"14")
   producer.produce(topic, b"14")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/victory", methods=['GET', 'POST'])
def victory():
   client.publish(topic,"15")
   producer.produce(topic, b"15")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/sleeping", methods=['GET', 'POST'])
def sleeping():
   client.publish(topic,"16")
   producer.produce(topic, b"16")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/confused", methods=['GET', 'POST'])
def confused():
   client.publish(topic,"17")
   producer.produce(topic, b"17")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/fart", methods=['GET', 'POST'])
def fart():
   client.publish(topic,"18")
   producer.produce(topic, b"18")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/fail", methods=['GET', 'POST'])
def fail():
   client.publish(topic,"19")
   producer.produce(topic, b"19")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/followMode", methods=['GET', 'POST'])
def followMode():
   client.publish(topic,"20")
   producer.produce(topic, b"20")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/retrieveMode", methods=['GET', 'POST'])
def retrieveMode():
   client.publish(topic,"21")
   producer.produce(topic, b"21")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/avoidObstacles", methods=['GET', 'POST'])
def avoidObstacles():
   client.publish(topic,"22")
   producer.produce(topic, b"22")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/dance", methods=["GET", "POST"])
def dance():
   client.publish(topic,"dance")
   # (topic, msg in bytes)
   producer.produce(topic, b"hola")
   return (""), 204


if __name__ == "__main__":
   #cliente mqtt setup
   client = mqtt.Client()
   client.username_pw_set(os.environ['MQTT_USERNAME'], os.environ['MQTT_PASSWORD'])
   client.on_connect = on_connect
   client.connect("172.18.0.2")
   client.loop_start()
   app.secret_key = 'super secret key'

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

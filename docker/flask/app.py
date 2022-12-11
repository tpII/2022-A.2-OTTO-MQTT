from flask import Flask, render_template, flash
import os
import paho.mqtt.client as mqtt
from confluent_kafka import Producer

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
topic = 'otto'
tipo = 'mosquitto' ##variable para saber con cual tipo de comunicacion estoy

def on_connect(client, userdata, flags, rc):
    client.publish('debug', "Flask conectado!")

@app.route("/")
def home():
    flash("Actualmente te comunicas a traves de Mosquitto con Otto!") ##mensaje que manda al iniciar
    return render_template('home.html')

@app.route("/kafka", methods=['GET', 'POST'])
def kafka():
   global tipo
   flash("Excelente eleccion, ahora te comunicas a traves de Kafka con Otto!") ##msj cuando cambia de tipo de comnunicacion
   if tipo=='mosquitto': ##cambio el tipo de comunicacion
      client.publish(topic,"cambiame a kafka")
      tipo='kafka'
   return render_template('home.html')

@app.route("/mosquitto", methods=['GET', 'POST'])
def mosquitto():
   global tipo
   flash("Excelente eleccion, ahora te comunicas a traves de Mosquitto con Otto!") ##msj cuando cambia de tipo de comnunicacion
   if tipo=='kafka': ##cambio el tipo de comunicacion
      producer.produce(topic, b"cambiame a mosquitto")
      tipo='mosquitto'
   return render_template('home.html')


@app.route("/posInicial", methods=['GET', 'POST'])
def posInicial():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto': 
      client.publish(topic,"00")
   else:
      producer.produce(topic, b"00")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/walkForward", methods=['GET', 'POST'])
def walkForward():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"01")
   else:
      producer.produce(topic, b"01")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/walkBackward", methods=["GET", "POST"])
def walkBackward():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"02")
   else:
      producer.produce(topic, b"02")
   return (""), 204 #con este se mantiene en la misma pag

@app.route("/turnRight", methods=['GET', 'POST'])
def turnRight():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"03")
   else:
      producer.produce(topic, b"03")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/turnLeft", methods=['GET', 'POST'])
def turnLeft():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"04")
   else:
      producer.produce(topic, b"04")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/bend", methods=['GET', 'POST'])
def bend():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"05")
   else:
      producer.produce(topic, b"05")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/shakeLeg", methods=['GET', 'POST'])
def shakeLeg():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"06")
   else:
      producer.produce(topic, b"06")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/moonwalker", methods=['GET', 'POST'])
def moonwalker():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"07")
   else:
      producer.produce(topic, b"07")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/crusaito", methods=['GET', 'POST'])
def crusaito():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"08")
   else:
      producer.produce(topic, b"08")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/flapping", methods=['GET', 'POST'])
def flapping():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"09")
   else:
      producer.produce(topic, b"09")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/swing", methods=['GET', 'POST'])
def swing():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"10")
   else:
      producer.produce(topic, b"10")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/tiptoeSwing", methods=['GET', 'POST'])
def tiptoeSwing():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"11")
   else:
      producer.produce(topic, b"11")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/upDown", methods=['GET', 'POST'])
def upDown():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"12")
   else:
      producer.produce(topic, b"12")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/happy", methods=['GET', 'POST'])
def happy():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"13")
   else:
      producer.produce(topic, b"13")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/sad", methods=['GET', 'POST'])
def sad():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"14")
   else:
      producer.produce(topic, b"14")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/victory", methods=['GET', 'POST'])
def victory():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"15")
   else:
      producer.produce(topic, b"15")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/sleeping", methods=['GET', 'POST'])
def sleeping():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"16")
   else:
      producer.produce(topic, b"16")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/confused", methods=['GET', 'POST'])
def confused():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"17")
   else:
      producer.produce(topic, b"17")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/fart", methods=['GET', 'POST'])
def fart():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"18")
   else:
      producer.produce(topic, b"18")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/fail", methods=['GET', 'POST'])
def fail():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"19")
   else:
      producer.produce(topic, b"19")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/followMode", methods=['GET', 'POST'])
def followMode():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"20")
   else:
      producer.produce(topic, b"20")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/retrieveMode", methods=['GET', 'POST'])
def retrieveMode():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"21")
   else:
      producer.produce(topic, b"21")
   return (''), 204 #con este se mantiene en la misma pag

@app.route("/avoidObstacles", methods=['GET', 'POST'])
def avoidObstacles():
   ##dependiendo del tipo de comunicacion actual, envio el msj al broker que corresponda
   if tipo=='mosquitto':
      client.publish(topic,"22")
   else:
      producer.produce(topic, b"22")
   return (''), 204 #con este se mantiene en la misma pag

if __name__ == "__main__":
   
   #cliente mqtt
   client = mqtt.Client()
   #Setea el nombre de usuario y la contraseña para acceder al broker mosquitto
   client.username_pw_set(os.environ['MQTT_USERNAME'], os.environ['MQTT_PASSWORD'])
   #define el comportamiento al iniciar la conexion
   client.on_connect = on_connect
   #inicia la conexion
   client.connect("172.18.0.2")
   client.loop_start()
   
   #clave de seguridad
   app.secret_key = 'super secret key'

   #productor kafka
   conf = {
      'bootstrap.servers': '172.18.0.26:9092' ,
      'security.protocol': 'PLAINTEXT',
   }
   producer = Producer(**conf)

   app.run(host="0.0.0.0", port=5000, debug=True)
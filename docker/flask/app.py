from flask import Flask, render_template, flash
from redis import Redis
import paho.mqtt.client as mqtt


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
redis = Redis(host='redis',port=6379)

topic = 'test'

def on_connect(client, userdata, flags, rc):
    client.publish(topic, "Cliente conectado. -Flask")

@app.route('/')
def home():
    flash("Actualmente te comunicas a traves de Mosquitto con Otto!")
    return render_template('home.html')

@app.route('/kafka', methods=['GET', 'POST'])
def kafka():
   flash("Excelente eleccion, ahora te comunicas a traves de Kafka con Otto!")
   client.publish(topic,"cambiame a kafka")
   return render_template('home.html')

@app.route('/mosquitto', methods=['GET', 'POST'])
def mosquitto():
   flash("Excelente eleccion, ahora te comunicas a traves de Mosquitto con Otto!")
   client.publish(topic,"cambiame a mosquitto")
   return render_template('home.html')


@app.route('/walkForward', methods=['GET', 'POST'])
def walkForward():
   client.publish(topic,"walk forward")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/walkRight', methods=['GET', 'POST'])
def walkRight():
   client.publish(topic,"walk right")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/walkLeft', methods=['GET', 'POST'])
def walkLeft():
   client.publish(topic,"walk left")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/walkBackward', methods=['GET', 'POST'])
def walkBackward():
   client.publish(topic,"walk backward")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/turnRight', methods=['GET', 'POST'])
def turnRight():
   client.publish(topic,"turnRight")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/turnLeft', methods=['GET', 'POST'])
def turnLeft():
   client.publish(topic,"turnLeft")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/bend', methods=['GET', 'POST'])
def bend():
   client.publish(topic,"bend")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/shakeLeg', methods=['GET', 'POST'])
def shakeLeg():
   client.publish(topic,"shakeLeg")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/moonwalker', methods=['GET', 'POST'])
def moonwalker():
   client.publish(topic,"moonwalker")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/crusaito', methods=['GET', 'POST'])
def crusaito():
   client.publish(topic,"crusaito")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/flapping', methods=['GET', 'POST'])
def flapping():
   client.publish(topic,"flapping")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/swing', methods=['GET', 'POST'])
def swing():
   client.publish(topic,"swing")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/tiptoeSwing', methods=['GET', 'POST'])
def tiptoeSwing():
   client.publish(topic,"tiptoeSwing")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/upDown', methods=['GET', 'POST'])
def upDown():
   client.publish(topic,"upDown")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/happy', methods=['GET', 'POST'])
def happy():
   client.publish(topic,"happy")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/sad', methods=['GET', 'POST'])
def sad():
   client.publish(topic,"sad")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/victory', methods=['GET', 'POST'])
def victory():
   client.publish(topic,"victory")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/sleeping', methods=['GET', 'POST'])
def sleeping():
   client.publish(topic,"sleeping")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/confused', methods=['GET', 'POST'])
def confused():
   client.publish(topic,"confused")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/fart', methods=['GET', 'POST'])
def fart():
   client.publish(topic,"fart")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/fail', methods=['GET', 'POST'])
def fail():
   client.publish(topic,"fail")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/followMode', methods=['GET', 'POST'])
def followMode():
   client.publish(topic,"followMode")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/retrieveMode', methods=['GET', 'POST'])
def retrieveMode():
   client.publish(topic,"retrieveMode")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/avoidObstacles', methods=['GET', 'POST'])
def avoidObstacles():
   client.publish(topic,"avoidObstacles")
   return (''), 204 #con este se mantiene en la misma pag



if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set('Flask', 'DefaultFlask')
    client.on_connect = on_connect
    client.connect('172.18.0.2')
    client.loop_start()
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=5000, debug=True)
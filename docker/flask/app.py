from flask import Flask
from redis import Redis
import paho.mqtt.client as mqtt
from flask import render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
redis = Redis(host='redis',port=6379)

topic = 'test'

def on_connect(client, userdata, flags, rc):
    client.publish(topic, "Cliente conectado. -Flask")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/walkForward', methods=['GET', 'POST'])
def walkForward():
   client.publish(topic,"walk forward")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/walkBackward', methods=['GET', 'POST'])
def walkBackward():
   client.publish(topic,"walk backward")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/walkRight', methods=['GET', 'POST'])
def walkRight():
   client.publish(topic,"walk right")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/walkLeft', methods=['GET', 'POST'])
def walkLeft():
   client.publish(topic,"walk left")
   return (''), 204 #con este se mantiene en la misma pag

@app.route('/dance', methods=['GET', 'POST'])
def dance():
   client.publish(topic,"dance")
   return (''), 204


if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set('Flask', 'DefaultFlask')
    client.on_connect = on_connect
    client.connect('172.18.0.2')
    client.loop_start()

    app.run(host='0.0.0.0', port=5000)
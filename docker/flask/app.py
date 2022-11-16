from flask import Flask
from redis import Redis
import paho.mqtt.client as mqtt
from flask import render_template

app = Flask(__name__)
redis = Redis(host='redis',port=6379)

topic = 'test'

def on_connect(client, userdata, flags, rc):
    client.publish(topic, "Cliente conectado. -Flask")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/walk', methods=['GET', 'POST'])
def walk():
   client.publish(topic,"walk")
   return (''), 204

@app.route('/dance', methods=['GET', 'POST'])
def dance():
   client.publish(topic,"dance")
   return (''), 204

if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set('Flask', 'DefaultFlask')
    client.on_connect = on_connect
    client.connect('172.19.0.3')
    client.loop_start()

    app.run(host='0.0.0.0', port=5000, debug=True)
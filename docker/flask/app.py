# compose_flask/app.py
from flask import Flask
from redis import Redis
from flask import render_template

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


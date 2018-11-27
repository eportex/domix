import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return datetime.datetime.now() + "Hello World! Test Äderung"
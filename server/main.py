import datetime
from flask import Flask
app = Flask(__name__)
x = datetime.datetime.now()

@app.route("/")
def hello():
    return x
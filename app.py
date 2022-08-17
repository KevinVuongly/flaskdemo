from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Tweede poging!</p>"

@app.route("/twwed")
def world():
    return "<p>Tweede scherm!!</p>"
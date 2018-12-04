from flask import Flask
app = Flask(__name__)

@app.route("/Hi")
def hi():
	return "Hi, How are you?"

@app.route("/")
def hello():
    return "Hello World!"
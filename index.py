from flask import flask

app = Flask(__name__)

@app.route('/')
def index:
    print("This is the home page")

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the home page'

@app.route('/about')
def about():
    return '<h2>Hey this is mt site</h2>'

if __name__ =="__main__":
    app.run(debug=True)

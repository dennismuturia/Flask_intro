from flask import Flask, request
#I will be dealing with HTTP requests both Get and Post

app = Flask(__name__)

#Let us implement the get and post method
@app.route('/')
def index():
    return 'Method used is %s' % request.method

@app.route('/bacon', methods = ['GET', 'POST'])
def bacon():
    if request.method == 'GET':
        return 'You are using the GET'
    else:
        return 'You are probably using POST'

@app.route('/about')
def about():
    return '<h2>Hey this is mt site</h2>'

@app.route('/profile/<username>')
def profile(username):
    return 'Hey there %s' % username

if __name__ =="__main__":
    app.run(debug=True)

from flask import Flask, request, render_template
#I will be dealing with HTTP requests both Get and Post

app = Flask(__name__)

#Let us implement the get and post method and using of templates
@app.route('/')
def index():
    return 'Method used is %s' % request.method



if __name__ =="__main__":
    app.run(debug=True)

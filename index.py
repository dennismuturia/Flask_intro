from flask import Flask, request, render_template
#I will be dealing with HTTP requests both Get and Post

app = Flask(__name__)

#Let us implement the get and post method and using of templates
#Lets incorporate another url in this index
@app.route('/')
@app.route('/<name>')
def index(name = None):
    return render_template("index.html", name=name)

if __name__ =="__main__":
    app.run(debug=True)

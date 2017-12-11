from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap
#I will install flask assets
#I will be dealing with HTTP requests both Get and Post

app = Flask(__name__)
bootstrap = Bootstrap(app)

#Let us implement the get and post method and using of templates
#Lets incorporate another url in this index
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
#Later on today I will try and incorporate bootstrap and route through the navigation bar
#Implementing flask assets in the project

#This will be the about page
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ =="__main__":
    app.run(debug=True)

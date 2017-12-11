from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

#Let us implement the get and post method and using of templates

@app.route('/')
def index():
    return render_template("index.html")
#Later on today I will try and incorporate bootstrap and route through the navigation bar

#This will be the about page
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ =="__main__":
    app.run(debug=True)

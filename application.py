import datetime
from flask import Flask, render_template, request

#app is just a variable that is like a reference to our application.
app = Flask(__name__)

@app.route("/")
def index():
    headline = "To be or not to be"
    return render_template("index.html", headline1=headline)

# @app.route("/<string:name>")
# def hello(name):
#     name=name.capitalize()
#     return f"Hello {name}"

@app.route("/isitnewyear")
def new_year():
    now = datetime.datetime.now()
    new_year = now.month==1 and now.day == 1
    return render_template("new_year.html", new_year = new_year)

@app.route("/credits")
def credits():
    names = ["Auro", "Aatmaj", "Divya", "Yukti"]
    return render_template("credits.html", names = names)

@app.route("/hello_form", methods=["POST","GET"])
def hello_form():
    if request.method=="GET":
        return "Please fill the form first!!"
    else:
        name = request.form.get("name_of_input_field")
        return render_template("hello_form.html", name=name)

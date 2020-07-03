from flask import Flask, render_template, request
from models import *

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:postgres@localhost/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

@app.route("/")
def index():
    flights=Flight.query.all();
    return render_template("index.html",flights=flights)

@app.route("/book")
def book():
    flights=Flight.query.all()
    return render_template("booking.html",flights=flights)

@app.route("/submit",methods=["POST"])
def submit():
    passenger_name=request.form.get("name")
    try:
        flight_id=int(request.form.get("flight_id"))
    except ValueError:
        message="Invalid Flight Reference"
        return render_template("error.html",message=message)
    if not check_id(flight_id):
        message="Flight not available"
        return render_template("error.html",message=message)
    else:
        flight=Flight.query.get(flight_id)

    if not check_name(passenger_name):
        message="Invalid Name"
        return render_template("error.html",message=message)

    flight.add_passenger(passenger_name)
    message=f"{passenger_name} successfully booked a flight from {flight.origin} to {flight.destination}"
    return render_template("success.html",message=message)

@app.route("/<int:flight_id>")
def flight_details(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        message="No such flight"
        return render_template("error.html",message=message)
    passengers=flight.passengers
    return render_template("flight_details.html",flight=flight,passengers=passengers)

def check_id(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return False
    else:
        return True

def check_name(name):

    count=0
    for char in name:
        if char.isalpha():
            count+=1
        if (not char.isspace()) and (not char.isalnum()):
            return False

    if(count<2):
        return False

    if(len(name)>20):
        return False

    return True

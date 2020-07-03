import csv

from flask import Flask, render_template, request
from models import *

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:postgres@localhost/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

def main():
    f = open("Lecture4/flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination,duration=duration)
        db.session.add(flight)
        print(f"Added flight from {flight.origin} to {flight.destination}, {flight.duration}min")
    db.session.commit()

if __name__=="__main__":
    with app.app_context():
        main()

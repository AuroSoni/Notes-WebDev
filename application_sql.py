from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app = Flask(__name__)
engine = create_engine("postgresql://postgres:postgres@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights")
    return render_template("book_flight.html", flights=flights)

@app.route("/flights")
def flights():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("list_flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = db.execute("SELECT * FROM flights WHERE id=:id",{"id":flight_id}).fetchone()
    passengers = db.execute("SELECT * FROM passengers WHERE flight_id=:id",{"id":flight_id}).fetchall()
    return render_template("flight_details.html",flight=flight,passengers=passengers)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight"""
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html")
    passenger_name = request.form.get("passenger_name")
    flight = db.execute("SELECT * FROM flights WHERE id=:flight_id",{"flight_id":flight_id}).fetchone()
    if flight == None or (not check(passenger_name)):
        return render_template("error.html")
    else:
        db.execute("INSERT INTO passengers (name,flight_id) VALUES (:name, :flight_id)",{"name":passenger_name, "flight_id":flight.id})
        db.commit()
        return render_template("book.html", flight=flight, passenger_name=passenger_name)

def check(string):
    alpha = 0
    for char in string:
        if char.isalpha():
            alpha+=1
    if(alpha<=2):
        return False
    elif len(string)>=20:
        return False
    else:
        return True

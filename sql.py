from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#'postgresql://user:password@hostname/database_name'
#"postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
engine = create_engine("postgresql://postgres:postgres@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT * FROM flights")
    for flight in flights:
        print(f"Flight: {flight.origin} to {flight.destination}, {flight.duration}min")

    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT * FROM flights WHERE id = :id",{"id":flight_id}).fetchone()

    if flight is None:
        print("Error: no such flight")
        return

    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",{"flight_id":flight_id}).fetchall()

    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)

    if len(passengers) == 0:
        print("No passengers.")

if __name__=="__main__":
    main()

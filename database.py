import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#'postgresql://user:password@hostname/database_name'
#"postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
engine = create_engine("postgresql://postgres:postgres@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

def insert():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader: # loop gives each column a name
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",{"origin": origin, "destination": destination, "duration": duration})
          # substitute values from CSV line into SQL command, as per this dict

        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()
# transactions are assumed, so close the transaction finished
def main():
    #insert()
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} min")

if __name__ == "__main__":
    main()

import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

engine = create_engine("postgresql://postgres:postgres@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

def create():
    db.execute("CREATE TABLE passengers(\
                id SERIAL PRIMARY KEY,\
                name VARCHAR NOT NULL,\
                flight_id INTEGER REFERENCES flights)")
    db.commit()

def insert():
    f = open("passengers.csv")
    reader = csv.reader(f)
    for name,flight_id in reader:
        db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",{"name":name, "flight_id":flight_id})
        print(f"Added passenger {name} to flight{flight_id}")
    db.commit()
def main():
    create()
    insert()

if __name__ =="__main__":
    main()

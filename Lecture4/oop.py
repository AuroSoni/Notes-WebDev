class Flight:

    counter=1

    def __init__(self, origin, destination, duration):
        self.id=Flight.counter
        Flight.counter+=1
        self.origin=origin
        self.destination=destination
        self.duration=duration
        self.passengers=[]

    def print_info(self):
        print(f"{self.origin} to {self.destination}, {self.duration} min")
        print("Passengers:")
        for passenger in self.passengers:
            passenger.print_info()
        print("\n")

    def delay(self, delay):
        self.duration+=delay

    def add_passenger(self,passenger_name):
        passenger = Passenger(name=passenger_name,flight_id=self.id)
        self.passengers.append(passenger)

class Passenger:
    def __init__(self,name,flight_id):
        self.name=name
        self.flight_id=flight_id

    def print_info(self):
        print(f"Passenger {self.name}")

def main():
    f1 = Flight("New York","Lima",540)
    f2 = Flight("New Delhi","Mumbai",100)
    f1.add_passenger("Tanuja Soni")
    f1.add_passenger("Surendra Soni")
    f1.add_passenger("Aatmaj Soni")
    f1.add_passenger("Auro Soni")

    f2.add_passenger("Amit Jain")
    f2.add_passenger("Yash Jain")
    f2.add_passenger("Shubhang Bhargav")

    f1.print_info()
    f2.print_info()

if __name__== "__main__":
    main()

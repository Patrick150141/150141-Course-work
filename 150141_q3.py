# Define the base Vehicle class
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"

# Define the Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return f"{super().display_info()}, Number of Seats: {self.number_of_seats}"

# Define the Truck class that inherits from Vehicle
class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return f"{super().display_info()}, Cargo Capacity: {self.cargo_capacity} tons"

# Define the Motorcycle class that inherits from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return f"{super().display_info()}, Engine Capacity: {self.engine_capacity} cc"

# Define the Fleet class to manage the fleet of vehicles
class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle with registration number {vehicle.registration_number} added successfully.")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(vehicle.display_info())

    def search_vehicle_by_registration(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number.lower() == registration_number.lower():
                print(f"Vehicle found: {vehicle.display_info()}")
                return
        print("Vehicle not found.")

# Demonstration of functionalities
def main():
    # Create a fleet instance
    fleet = Fleet()

    # Add vehicles to the fleet
    car = Car("CAR123", "Toyota", "Corolla", 5)
    truck = Truck("TRK456", "Ford", "F-150", 10)
    motorcycle = Motorcycle("MOTO789", "Honda", "CBR600", 600)

    fleet.add_vehicle(car)
    fleet.add_vehicle(truck)
    fleet.add_vehicle(motorcycle)

    # Display all vehicles
    print("\nDisplaying all vehicles:")
    fleet.display_all_vehicles()

    # Search for a vehicle by registration number
    print("\nSearching for vehicle with registration number 'TRK456':")
    fleet.search_vehicle_by_registration("TRK456")

    print("\nSearching for vehicle with registration number 'NOTEXIST':")
    fleet.search_vehicle_by_registration("NOTEXIST")

if __name__ == "__main__":
    main()

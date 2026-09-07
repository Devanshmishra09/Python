# 5. Create an Employee Payroll System.
#    Implement different employee types such as FullTimeEmployee, PartTimeEmployee,
#    and ContractEmployee.
#    Calculate salary differently for each employee type

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method.")
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
class ContractEmployee(Employee):
    def __init__(self, name, employee_id, contract_amount):
        super().__init__(name, employee_id)
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount
object1 = FullTimeEmployee("Alice", 101, 5000)
object2 = PartTimeEmployee("Bob", 102, 20, 80)
object3 = ContractEmployee("Charlie", 103, 3000)
objects = [object1, object2, object3]
for employee in objects:
    print(f"Employee: {employee.name}, ID: {employee.employee_id}, Salary: ${employee.calculate_salary():.2f}") 


# 6. Design a Vehicle Rental System.
#    Create Vehicle, Customer, Rental, and RentalService classes.
#    Implement vehicle booking, return, availability checking, and rental cost calculation.

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, rental_rate):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.rental_rate = rental_rate
        self.is_available = True

    def __str__(self):
        return f"{self.vehicle_type} (ID: {self.vehicle_id}) - Rate: ${self.rental_rate}/day"
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"
class Rental:
    def __init__(self, vehicle, customer, rental_days):
        self.vehicle = vehicle
        self.customer = customer
        self.rental_days = rental_days
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        return self.vehicle.rental_rate * self.rental_days

    def __str__(self):
        return f"Rental: {self.vehicle} rented by {self.customer} for {self.rental_days} days. Total Cost: ${self.total_cost:.2f}"
    
class RentalService:
    def __init__(self):
        self.vehicles = []
        self.rentals = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle added: {vehicle}")

    def check_availability(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle.is_available
        return False

    def rent_vehicle(self, vehicle_id, customer, rental_days):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id and vehicle.is_available:
                rental = Rental(vehicle, customer, rental_days)
                self.rentals.append(rental)
                vehicle.is_available = False
                print(f"Vehicle rented: {rental}")
                return rental
        print(f"Vehicle ID {vehicle_id} is not available for rent.")
        return None

    def return_vehicle(self, vehicle_id):
        for rental in self.rentals:
            if rental.vehicle.vehicle_id == vehicle_id:
                rental.vehicle.is_available = True
                self.rentals.remove(rental)
                print(f"Vehicle returned: {rental.vehicle}")
                return
        print(f"No active rental found for Vehicle ID {vehicle_id}.")
object1 = Vehicle("V001", "Car", 50)
object2 = Vehicle("V002", "Bike", 20)
object3 = Vehicle("V003", "Truck", 100)
customer1 = Customer("Alice", "C001")
rental_service = RentalService()
rental_service.add_vehicle(object1)
rental_service.add_vehicle(object2)
rental_service.add_vehicle(object3)
rental_service.rent_vehicle("V001", customer1, 3)   
rental_service.return_vehicle("V001")

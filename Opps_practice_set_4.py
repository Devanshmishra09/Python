# 7. Create a Food Delivery System.
#    Implement Customer, Restaurant, FoodItem, Cart, and Order classes.
#    Support multiple restaurants and order status management.

from Opps_practice_set_2 import Cart


class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food_item(self, food_item):
        self.menu.append(food_item)
        print(f"Food item added to {self.name}: {food_item}")

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(item)
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
        print(f"Customer created: {self.name}")

    def add_to_cart(self, food_item, quantity):
        self.cart.add_food_item(food_item, quantity)
class Order:
    def __init__(self, customer, restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.status = "Pending"
        self.total_amount = 0

    def calculate_total(self):
        for food_item, quantity in self.customer.cart.items:
            self.total_amount += food_item.price * quantity
        print(f"Total amount for order from {self.restaurant.name}: ${self.total_amount:.2f}")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order status updated to: {self.status}")
class FoodDeliverySystem:
    def __init__(self):
        self.restaurants = []
        self.customers = []
        print("Food Delivery System initialized.")

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)
        print(f"Restaurant added: {restaurant.name}")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer added: {customer.name}")

object1 = FoodItem("Pizza", 12.99)
object2 = FoodItem("Burger", 8.99)
object3 = FoodItem("Pasta", 10.99)
restaurant1 = Restaurant("Italian Delight")
restaurant1.add_food_item(object1)
restaurant1.add_food_item(object3)
restaurant2 = Restaurant("Fast Food Hub")
restaurant2.add_food_item(object2)
customer1 = Customer("Alice")
customer1.add_to_cart(object1, 2)
customer1.add_to_cart(object2, 1)
customer1.add_to_cart(object3, 1)
customer1.cart.display_cart()
order1 = Order(customer1, restaurant1)
order1.calculate_total()
order1.update_status("Preparing")
object = FoodDeliverySystem()
object.add_restaurant(restaurant1)
object.add_restaurant(restaurant2)
object.add_customer(customer1)


#  8. Design a Hospital Management System.
#    Create Doctor, Patient, Appointment, and Hospital classes.
#    Implement appointment booking, cancellation, and doctor availability

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.appointments = []

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        print(f"Appointment added for {self.name}: {appointment}")

    def cancel_appointment(self, appointment):
        if appointment in self.appointments:
            self.appointments.remove(appointment)
            print(f"Appointment canceled for {self.name}: {appointment}")
        else:
            print(f"No such appointment found for {self.name}.")
class Patient:
    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id
        self.appointments = []

    def __str__(self):
        return f"Patient: {self.name} (ID: {self.patient_id})"

    def book_appointment(self, doctor, appointment):
        doctor.add_appointment(appointment)
        self.appointments.append(appointment)
        print(f"{self.name} booked an appointment with {doctor.name}.")
class Appointment:
    def __init__(self, doctor, patient, date_time):
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time

    def __str__(self):
        return f"Appointment with {self.doctor.name} for {self.patient.name} on {self.date_time}"
class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor added: {doctor}")

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient added: {patient}")

    def display_doctors(self):
        print(f"Doctors in {self.name}:")
        for doctor in self.doctors:
            print(doctor)

    def display_patients(self):
        print(f"Patients in {self.name}:")
        for patient in self.patients:
            print(patient)
class HospitalManagementSystem:
    def __init__(self):
        self.hospitals = []
        print("Hospital Management System initialized.")

    def add_hospital(self, hospital):
        self.hospitals.append(hospital)
        print(f"Hospital added: {hospital.name}")
object1 = Doctor("Smith", "Cardiology")
object2 = Doctor("Johnson", "Neurology")
object3 = Patient("Alice", "P001")
hospital1 = Hospital("City Hospital")
hospital1.add_doctor(object1)
hospital1.add_doctor(object2)
hospital1.add_patient(object3)
hospital_system = HospitalManagementSystem()
hospital_system.add_hospital(hospital1)
hospital1.display_doctors()
hospital1.display_patients()
hospital1.doctors[0].add_appointment(Appointment(object1, object3, "2024-06-15 10:00 AM"))
hospital1.doctors[0].cancel_appointment(Appointment(object1, object3, "2024-06-15 10:00 AM"))
hospital1.doctors[0].add_appointment(Appointment(object1, object3, "2024-06-15 10:00 AM"))
hospital1.doctors[0].cancel_appointment(Appointment(object1, object3, "2024-06-15 10:00 AM"))



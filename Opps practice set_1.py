# 1. Design a Library Management System using OOP.
#    Implement Book, Member, and Library classes.
#    Support issue book, return book, search book, and availability tracking.


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member added: {member}")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print(f"Book not found: {title}")
        return None
    
    def check_availability(self, title):
        book = self.search_book(title)
        if book:
            return book.is_available
        return False

object = Library()
object.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"))
object.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780061120084"))
object.add_member(Member("Alice", "M001"))
object.add_member(Member("Bob", "M002"))
object.search_book("The Great Gatsby")
object.check_availability("The Great Gatsby")
object.members[0].borrow_book(object.books[0])  


#  2. Design a Parking Lot System.
#    Create classes for Vehicle, ParkingSpot, and ParkingLot.
#    Support different vehicle types and calculate parking fees based on duration.


class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, spot_id, vehicle_type):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.is_occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle):
        if not self.is_occupied and vehicle.vehicle_type == self.vehicle_type:
            self.is_occupied = True
            self.vehicle = vehicle
            print(f"Vehicle {vehicle.license_plate} parked in spot {self.spot_id}.")
        else:
            print(f"Cannot park vehicle {vehicle.license_plate} in spot {self.spot_id}.")

    def remove_vehicle(self):
        if self.is_occupied:
            print(f"Vehicle {self.vehicle.license_plate} removed from spot {self.spot_id}.")
            self.is_occupied = False
            self.vehicle = None
        else:
            print(f"No vehicle to remove from spot {self.spot_id}.")
            
class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_parking_spot(self, spot):
        self.spots.append(spot)
        print(f"Parking spot added: {spot.spot_id} for {spot.vehicle_type} vehicles.")

    def find_available_spot(self, vehicle_type):
        for spot in self.spots:
            if not spot.is_occupied and spot.vehicle_type == vehicle_type:
                return spot
        print(f"No available spots for {vehicle_type} vehicles.")
        return None

    def calculate_parking_fee(self, duration_hours):
        rate_per_hour = 5  # Example rate
        return duration_hours * rate_per_hour
class ParkingLotSystem:
    def __init__(self):
        self.parking_lot = ParkingLot()

    def park_vehicle(self, vehicle):
        spot = self.parking_lot.find_available_spot(vehicle.vehicle_type)
        if spot:
            spot.park_vehicle(vehicle)

    def remove_vehicle(self, license_plate):
        for spot in self.parking_lot.spots:
            if spot.is_occupied and spot.vehicle.license_plate == license_plate:
                spot.remove_vehicle()
                return
        print(f"Vehicle with license plate {license_plate} not found in the parking lot.")
 
object = ParkingLotSystem()
object.parking_lot.add_parking_spot(ParkingSpot("A1", "Car"))   
object.parking_lot.add_parking_spot(ParkingSpot("B1", "Motorcycle"))
car = Vehicle("ABC123", "Car")
object.park_vehicle(car)
object.remove_vehicle("ABC123")

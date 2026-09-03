# 9. Food Delivery System — Inheritance + Polymorphism

# Create a DeliveryPartner class with:
# - name
# - base_salary

# Create:
# - BikeDelivery
# - CarDelivery
# - CycleDelivery

# Requirements:
# - Create a calculate_earnings() method.
# - Override it in each child class.
# - Each delivery type should calculate earnings differently.
# - Display the final earnings of each delivery partner

class DeliveryPartner:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
        self.earnings = 0

    def calculate_earnings(self):
        pass
class BikeDelivery(DeliveryPartner):
    def calculate_earnings(self, distance):
        self.earnings = self.base_salary + (distance * 5)  # Example: $5 per km
        print(f"{self.name} earned {self.earnings} using Bike Delivery.")
class CarDelivery(DeliveryPartner):
    def calculate_earnings(self, distance):
        self.earnings = self.base_salary + (distance * 10)  # Example: $10 per km
        print(f"{self.name} earned {self.earnings} using Car Delivery.")    
class CycleDelivery(DeliveryPartner):
    def calculate_earnings(self, distance):
        self.earnings = self.base_salary + (distance * 2)  # Example: $2 per km
        print(f"{self.name} earned {self.earnings} using Cycle Delivery.")

obj=BikeDelivery("Shubh",1000)
obj.calculate_earnings(50)  
ob=CarDelivery("Devansh",2000)
ob.calculate_earnings(30)
O=CycleDelivery("Shivam",500)
O.calculate_earnings(20)


# 10. Online Notification System — Abstraction + Polymorphism

# Create an abstract class Notification with:

# send(message)

# Create:
# - EmailNotification
# - SMSNotification
# - PushNotification

# Requirements:
# - Each class should implement send() differently.
# - Create one common function to send a notification.
# - The function should work with any Notification object.
# - Use abstraction and polymorphism

from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailNotification(Notification):
    def send(self,message):
        print(f"Sending Email: {message}")
class SMSNotification(Notification):
    def send(self,message):
        print(f"Sending SMS: {message}")
class PushNotification(Notification):
    def send(self,message):
        print(f"Sending Push Notification: {message}")
class NotificationSender:
    def send_notification(self, notification, message):
        notification.send(message)
sender = NotificationSender()
sender.send_notification(EmailNotification(), "Hello via Email!")
sender.send_notification(SMSNotification(), "Hello via SMS!")
sender.send_notification(PushNotification(), "Hello via Push Notification!")
    

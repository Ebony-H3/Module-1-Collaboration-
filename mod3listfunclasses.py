#Ebony Harris
#Mod3listfunclasses.py
#This is an app that allows user to enter a car details then it will display the car details back to the user

#This is the parent class 
#
class vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# This is the child class
#the child class inherits the parent class vehicle
class automobile(vehicle):
    def __init__(self,year,make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Identifies the vehicle type
vehicle_type = input("Please enter the type of vehicle you have(car,suv,turck...etc): ")
#Deatils about the vehicle entered here
year = input("The vehicles year: ")
make = input("Make of the vehicle: ")
model = input("Vehicle model: ")
doors = input("Number of doors(2 or 4): ")
roof = input("Type of roof(sunroof or solid): ")

#Create the object using input variable
users_car = automobile(year, make, model, doors, roof)

print("Here are the details of your vehicle: ")

#displays to the user what they just entered about their vehicle a car
print("Type of vehicle:", users_car.vehicle_type)
print("Year of vehicle:", users_car.year)
print("Make of vehicle:", users_car.make) 
print("Model of vehicle:", users_car.model)
print("Number of doors:", users_car.doors)
print("Type of roof:",  users_car.roof)
"""
Object Oriented Programming is one of the most effective approaches to writing software.
In OOP's we write classes which represent real world things and situations, we create objects based on the classes
When we write a class we define a general behaviour that a whole category of objects can have
"""

"""
Making an object from a class is called is called "instantiation"
We work with instances of a class

"""

# #............................Creating and using a class........................#
# """
# Here we write a class about dogs, defining their general characteristics!
#
# """
# class Dog:
#     """A simple attempt to model a Dog!"""
#
#     def __init__(self, name, age):
#         """Initialize name and age attribute"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting!")
#
#     def roll_over(self):
#         """Simulate a dog rolling over to a command"""
#         print(f"{self.name} rolled over!")
#
# """
# A function that is a part of a class is called a method.
# """

# ..............................Making an Instance from a class...................#

# my_dog = Dog('Brownie', 6)
# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} year old")
#
# my_dog.sit()
# my_dog.roll_over()
#
#
# #............................Creating Multiple Instances.........................#
# #Instance 1
# my_dog = Dog('Brownie', 6)
# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} year old")
#
# my_dog.sit()
# my_dog.roll_over()
# #Instance 2
# your_dog = Dog('Millie', 8)
# print(f"My dog's name is {your_dog.name}")
# print(f"My dog is {your_dog.age} year old")
#
# your_dog.sit()
# your_dog.roll_over()

# ..........................Working with Classes and Instances......................#

# """" The Class Car """
#
# class Car:
#     """ A simple attempt to represent a car """
#
#     """"
# Classes are used to represent the real-world situations.
# Instances are created by the class
# We will modify the attributes associated with the instances
# """
#     def __init__(self, car_name, model_year, maker):
#         self.car_name = car_name
#         self.model_year = model_year
#         self.model = maker
#
#     def describe_car(self):
#         """
#         Describes the car with the given attribute in the defination of the attribute
#         :return: Neatly formatted car description of the car
#         """
#         long_name = f"{self.model_year} {self.car_name} {self.model}"
#         return long_name.title()
#
# """
# Adding a new instance in the class
# We will add a new instance which will read the odometer reading of the car and then can show it to us when
# needed.
# """
#
# class Car:
#     """ A simple attempt to represent a car """
#
#     def __init__(self, car_name, model_year, maker):
#         self.car_name = car_name
#         self.model_year = model_year
#         self.model = maker
# #.................................................................................#
#         self.odometer_reading = 0
# #.................................................................................#
#     def read_odometer(self):
#         """
#         Print a statement tellin gthe current reading of the odometer
#         :return: A string that tells the odometer reading
#         """
#         print(f"The current reading of your {self.car_name} is {self.odometer_reading}")
# #..................................................................................#
#     def describe_car(self):
#         """
#         Describes the car with the given attribute in the defination of the attribute
#         :return: Neatly formatted car description of the car
#         """
#         long_name = f"{self.model_year} {self.car_name} {self.model}"
#         return long_name.title()
#
# my_car = Car('A5', '2019', 'Audi')
# print(my_car.describe_car())
# my_car.read_odometer()
#
#
# """ How to modify the attribute value?
#
#     What if I want to change the Odometer reading, how will I update the value of that attribute?
# Ans: Attribute can be modified using 3 methods
#                                             1. Change the value directly through the instance
#                                             2. Set the value through a method
#                                             3. Create a method to update the value eg: Increment or decrement
# """
#
# """ 1. The direct method (update the value of the reading through an instance) """
# class Car:
#     """ A simple attempt to represent a car """
#
#     def __init__(self, car_name, model_year, maker):
#         self.car_name = car_name
#         self.model_year = model_year
#         self.model = maker
# #.................................................................................#
#         self.odometer_reading = 0
# #.................................................................................#
#     def read_odometer(self):
#         """
#         Print a statement tellin gthe current reading of the odometer
#         :return: A string that tells the odometer reading
#         """
#         print(f"The current reading of your {self.car_name} is {self.odometer_reading}")
# #..................................................................................#
#     def describe_car(self):
#         """
#         Describes the car with the given attribute in the defination of the attribute
#         :return: Neatly formatted car description of the car
#         """
#         long_name = f"{self.model_year} {self.car_name} {self.model}"
#         return long_name.title()
#
# my_car = Car('A5', '2019', 'Audi')
# print(my_car.describe_car())
# #....................................................................................#
# my_car.odometer_reading = 25
# my_car.read_odometer()
# #....................................................................................#
#
# """ 2. Setting a value through a  method """
# class Car:
#     """ A simple attempt to represent a car """
#
#     def __init__(self, car_name, model_year, maker):
#         self.car_name = car_name
#         self.model_year = model_year
#         self.model = maker
# #.................................................................................#
#         self.odometer_reading = 0
# #.................................................................................#
#     def read_odometer(self):
#         """
#         Print a statement tellin gthe current reading of the odometer
#         :return: A string that tells the odometer reading
#         """
#         print(f"The current reading of your {self.car_name} is {self.odometer_reading}")
#
#     def update_odometer(self, milage):
#         """
#         Updates the reading of the odometer reading by taking a new value
#         :return: A attribute which takes
#         """
#         self.odometer_reading = milage
# #..................................................................................#
#     def describe_car(self):
#         """
#         Describes the car with the given attribute in the defination of the attribute
#         :return: Neatly formatted car description of the car
#         """
#         long_name = f"{self.model_year} {self.car_name} {self.model}"
#         return long_name.title()
#
# my_car = Car('A5', '2019', 'Audi')
# print(my_car.describe_car())
# my_car.read_odometer()
# #..................................................................................#
# my_car.update_odometer('65')
# #.................................................................................#
# my_car.read_odometer()"

""" 3. Create a method to update the value Eg: Increment or Decrement """
# class Car:
#     """ A simple attempt to represent a car """
#
#     def __init__(self, car_name, model_year, maker):
#         self.car_name = car_name
#         self.model_year = model_year
#         self.model = maker
# #.................................................................................#
#         self.odometer_reading = 0
# #.................................................................................#
#     def read_odometer(self):
#         """
#         Print a statement tellin gthe current reading of the odometer
#         :return: A string that tells the odometer reading
#         """
#         print(f"The current reading of your {self.car_name} is {self.odometer_reading}")
#
#     def update_odometer(self, milage):
#         """
#         Updates the reading of the odometer reading by taking a new value
#         Check if the user is trying to roll back the odometer's values if yes
#         print a statement that they can't.
#         :return: A attribute which takes in milage
#         """
#         if milage >= self.odometer_reading:
#             self.odometer_reading = milage
#         else:
#             print(f" You cannot roll back Odometer's readings ")
#
#     def increment_odometer(self, miles):
#         """
#         Add's the number of miles to the current odometer reading
#         :param miles: Integer value that represents the additional miles needed to be updated on the odometer
#         :return: updated odometer readings
#         """
#         self.odometer_reading += miles
# #..................................................................................#
#     def describe_car(self):
#         """
#         Describes the car with the given attribute in the defination of the attribute
#         :return: Neatly formatted car description of the car
#         """
#         long_name = f"{self.model_year} {self.car_name} {self.model}"
#         return long_name.title()
#
# my_car = Car('A8', '2019', 'Audi')
# print(my_car.describe_car())
#
# my_car.read_odometer()
# my_car.update_odometer(75)
# my_car.increment_odometer(80)
# my_car.read_odometer()


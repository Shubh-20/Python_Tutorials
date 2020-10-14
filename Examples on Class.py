""" Here we have simple examples based on classes """
#.........................................Example(1)................................#
"""
Make a class called Restaurant. It stores two attribute in it __init__() method which are
1. restaurant_name
2. cuisine_type

Make a method called "describe_restaurant" which describes the two attributes
Make a method called "open_restaurant" which prints that the restaurant is open
"""
# class Restaurant:
#     """Displays some attributes about a restaurant"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize the functions"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Function that describes the resutaurant types"""
#         print(f"The name of the restaurant is {self.restaurant_name}\nIt serves {self.cuisine_type} food!")
#
#     def open_restaurant(self):
#         """Function tells that the restaurant is open"""
#         print(f"{self.restaurant_name} is now OPEN!")
#
#
# #This is called an Instance
# new_restaurant = Restaurant('Marriot', 'Chinese')
# new_restaurant.describe_restaurant()
# new_restaurant.open_restaurant()
# print(f"I love the restaurant on the 5th street, its name is {new_restaurant.restaurant_name}")

#........................................Example (2)........................................................#
class User:
    """ This class stores the general information about the user"""

    def __init__(self, first_name, last_name):
        """Initialize the function"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_name(self):
        """  Describes the user with its name """
        print(f"User's name is {self.first_name} {self.last_name}")

    def greet_user(self):
        """ Greet the user with a soft sweet message """
        print(f"Hello! {self.first_name}. Its nice to meet you!")

new_user = User('Shubham', 'Mishra')


new_user.describe_name()
new_user.greet_user()
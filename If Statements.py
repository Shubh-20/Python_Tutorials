# Programming often involves examining a set of conditions and deciding which action to take based on those
# conditions. Pthins if statement allows you to examine the current state of the program and respond appropriately to that state.

# Example 1
# cars = ['BMW','AUDI','VW','MERCEDES']
# for car in cars:
#     if car == 'BMW':
#         print(car.lower())
#     else:
#         print(car.upper())

# Check for Inequalities
#
# test = 'Positive'
# if test != 'Negative':
#     print('Hold the positive state')

# Checking multiple conditions

# a_0 = 21
# b_0 = 30
#
# var = a_0 >= 18 and b_0 >= 18
# print(var)

#Checking for a value in list
# List = ['a','b','c']
# var = 'd' in List
# print(var)
#Checking for value not in list
# banned_user = ['a','b','c']
# user = 'd'
# if user not in banned_user:
#     print(f"{user.title()}, you can post your response")

#if-else statements
# age = 17
# if age>=18:
#     print("You are welcome to vote! Please vote carefully")
# else:
#     print("You need to be 18 atleast to vote!")
#Use of Elif statement
# age = 9
# if age < 4 :
#     print("You'r ticket is on us!")
# elif age < 18:
#     print("You have to pay 50% of the ticket cost")
# else:
# #     print("You need to pay the whole cost of the ticket!")
# #Testing Multiple conditions
# toppings_requested = ['mushroom','olives','Chilli']
# if 'mushroom' in toppings_requested:
#     print('Adding Mushrooms')
# if 'olives' in toppings_requested:
#     print('Adding Olives')
# print('\nYour pizza is getting ready')
#Using a list with a loop
# request_topping = ['mushroom','green peppers','olives']
# for request_topping in request_topping:
#     print(f"Adding {request_topping.title()}")
# print("Your pizza is being prepared!")
# requested_topping = ['Mushroom','Olives','Chilli']
# if requested_topping == 'Green Pepper':
#     print("Sorry we are out of Green Pepper!")
# else:
#     print("Adding requested topping to your pizza!")
# print("Your pizza is being prepared!")
requested_topping = []
if requested_topping:
    for requested_topping in requested_topping:
        print("Adding requested topping")
else:
        print("Are you sure you want an empty pizza!")
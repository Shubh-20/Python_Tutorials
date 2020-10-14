#.......................................Movie Tickets...........................
#If age < 3: ticket is free
#If age 12=>3: ticket costs 10$
#If age <12: ticket costs 15$
#Write a loop to ask the age and print a message with price

# age = input("\nPlease Enter your age: ")
# age = int(age)
# if age <= 3:
#     print("\n You can enjoy the movie for free")
# elif age > 3 and age <= 12:
#     print("\n Your ticket cost is 10$")
# elif age > 12:
#     print("\nYour ticket cost is 15$")

#.......................................Three Exits...............................
#........................Creating a Poll by Filling a dictionary by user input......................
# responses = {}
#
# #Set a flag to show the status of the poll
# polling_active = True
#
# while polling_active:
#     #Prompt the user for name and the mountain they would like to climb
#     name = input("\nWhat's your name? ")
#     mountain = input("\nWhich mountain would you like to climb? ")
#
#     #Storing the responses for mountain along with name in a dictionary
#     responses[name] = mountain
#
#     #Asking if they would like for someone else to take the poll
#     repeat = input("\nWould your friend like to take this poll? (Yes/No): ")
#     if repeat == 'No':
#         polling_active = False
# #Polling is complete, show the results
# print("\n............The polling results............")
# for name, mountain in responses.items():
#     print(f"\t{name} would like to climb {mountain}")

#............................The Sandwich Shop......................................
#
# ordered_sandwiches = ['Tuna','Turnkey','Chicken','McAloo','pastrami','aloo','pastrami','pastrami']
# prepared_sandwiches = []
# print("Sorry we are out of Pastramis")
# while 'pastrami' in ordered_sandwiches:
#     ordered_sandwiches.remove('pastrami')
# print(ordered_sandwiches)
#
# while ordered_sandwiches:
#     current_sandwiches = ordered_sandwiches.pop()
#     print(f"\nI am preparing your {current_sandwiches} sandwich!")
#
#
#     prepared_sandwiches.append(current_sandwiches)
# print(f"\nAll the sandwiches made are: ")
# for sandwiches in prepared_sandwiches:
#     print(sandwiches.title())

#....................................Dream Vacation Poll................................
# dreams = {}
# poll_active = True
# while poll_active:
#     name = input("\nWhat is your name? ")
#     location = input("\nWhat place would you like to go for vacation: ")
#
#     dreams[name] = location
#
#     repeat = input("would your friend like to take the poll? (Y/N) ")
#     if repeat == 'N':
#         poll_active = False
# print("\n..................Poll Results.............")
# for name,location in dreams.items():
#     print(f"{name.title()} would like to go to {location} for a vacation!")

#Dictionaries  are collection of "Key-Value" pairs, each key is connected to a value.The key
# #value can be a number, list, string or any object in python.
#
#
# alien_0 = {'color':'green','points':5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

#Staring with an empty dictionary and then adding values to it.
# alien_0 = {}
# alien_0['x_cordinate'] = 0
# alien_0['y_cordinate'] = 25
# print(alien_0)

# Modifying the value in a dictionary
# alien_0 = {'color':'green'}
# print(f"The alien is of {alien_0['color']}.")
#
# alien_0['color'] = 'yellow'
# print(f"Now the color of the alien is {alien_0['color']}.")

#Example of tracking the movement of the aliens
# alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
# alien_0['speed'] = 'fast'
# print(f"Original position of the alien is {alien_0['x_position']}.")
#Now move the alien to the right
#Determine how far to move the alien based on the current speed
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# # The new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"The new position of the alien is {alien_0['x_position']}.")

#Removing a Key:Value pair from a dictionary
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# A dictionary of similar objects
# favorite_languages = {
#     'jen': 'python',
#     'Shubham': 'python',
#     'lake': 'ruby',
#     'phil': 'Python',
# }
# Collegues = ['jen', 'phil']
# for name in favorite_languages:
#     print(f"Hello there {name.title()}")
# if name in Collegues:
#     language = favorite_languages[name].title()
#     print(f"Hey! {name.title()}, I see you like {language.title()}")

#Looping through a Dictionaries
#Example of storing data from a user for a website
# user_0 = {
#     'username':'eframi',
#     'first':'Shubham',
#     'last':'Mishra',
# }
# for key, value in user_0.items():
#     print(f"\nKey:{key}")
#     print(f"\nValue:{value}")
# Looping through dictionary's keys in a perticular order.
# favorite_languages = {
#     'jen': 'python',
#     'Shubham': 'python',
#     'lake': 'ruby',
#     'phil': 'Python',
# }
# for name in sorted(favorite_languages):
#     print(f"{name.title()} Thank You for taking our poll!")

# Looping through Values of the Dictionaries

# print("The following languages have been mentioned in the poll:")
# for languages in set(favorite_languages.values()):
#     print(languages.title())

# major_rivers = {'Ganga':'Bihar','Yamuna':'Jammu','Godavari':'MP'}
# for river, state in major_rivers.items():
#     # print(f"River {river.title()} flow in state {state.title()}")
#     print(f"{river.title()}")
# language_poll = {'Sam': 'Python','jen': "C", "David": "Ruby", "Rajesh": "C++","Julie": "Javascript"}
# pending_list = ["sam","crank","mathias"]
# for alias, prog_lan in language_poll.items():
#     print(f"Hey there {alias.title()},we see you like {prog_lan.title()}.\nThank You for taking our poll!")
#

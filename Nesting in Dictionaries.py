# alien_0 = {'color':'green','points':5}
# alien_1 = {'color':'yellow','points':10}
# alien_2 = {'color':'blue','points':20}
#
# aliens = [alien_0,alien_1,alien_2]# we can store dictionaries in a list, list in a dictionary or dictionary in a dictionary
#
# for alien in aliens:
#     print(alien)
#Empty list for storing aliens
aliens = []

#make 30 new green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'Green','point':5,'speed':'slow'}
#     aliens.append(new_alien)
#
# # for alien in aliens[:5]:
# #     print(alien)
# # print(f"The total number of aliens created : {len(aliens)}")
#
# for alien in aliens[:3]:
#     if alien['color'] == 'Green':
#         alien['color'] = 'Yellow'
#         alien['point'] = 10
#         alien['speed'] = 'medium'
# for alien in aliens[:5]:
#     print(alien)
#
# for alien in aliens[:3]:
#     if alien['color'] == 'Yellow':
#         alien['color'] = 'red'
#         alien['point'] = 15
#         alien['speed'] = 'fast'
# for alien in aliens[:5]:
#     print(alien)
# Storing a list into a dictionary: Taking a online Pizza order and storing it and then providing the order summary

# pizza = {
#     'crust':'thick',
#     'toppings':['mushroom','extra cheese'],
#
# }
# #Summarize the order
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       f"with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")
# favorite_languages = {
#      'jen': ['python','ruby'],
#      'Shubham': ['python', 'C'],
#      'lake': ['ruby'],
#      'phil': ['Python', 'C++']
#  }
# for names, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f"{names.title()} likes these languages:")
#         for language in languages:
#             print(f"\t{language.title()}")
#     else:
#          print(f"{names.title()}'s favourite language is:")
#
#          for language in languages:
#              print(f"\t{language.title()}")

# Dictionary Inside a Dictionary
# username is the key and then a dictionary is assigned as a value containing the information about that user.
users = {
    'aeinstein':{'first':'albert','last':'einstein','location':'UK'},
    'mcurie':{'first':'marie','last':'curie','location':'USA'},
}

for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = f"{user_info['location']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")



# .................(1)...................
# def display_message():
#     """Displays a sentence"""
#     print("I am learning about functions in this chapter!")
#
# display_message()
# ..................(2)..................
# def favourite_book(book):
#     """Displays a persons favourite book"""
#     print(f"One of my favourite book is {book.title()}")
#
# favourite_book("alice in the wonderland")
# ..................(3) make_shirt Function..................#
# def make_shirt(size = 'L', message = 'I love Python'):
#     """ Takes in size and message to be printed on the shirt """
#     print(f"Your Tshirt is of size '{size}' and the message to be printed on it is '{message}'")
#
# make_shirt('M','I do not Love Python')
# ....................(3) City and Country....................#
# def city_and_Contry(city_name,country_name):
#     """Gives a city and the country that city is in"""
#     print(f'\n"{city_name}, {country_name}"')
#
#
# city_and_Contry('Mumbai','India')
# city_and_Contry('Berlin','Germany')

# ......................(4) ALbums............................#
# def make_album(artist_name, album_title, songs=None):
#     """Generates a dictionary with the name of the artist and the title of album"""
#     album = {'artist_name': artist_name, 'album_title': album_title}
#     #Adding a new item to list as 'songs'
#     if songs:
#         album['songs'] = songs
#     return album
#
#
# new_album = make_album('Atif Aslam', 'Doorie', 6)
#
# print(new_album)

# ...........................(5) make movies......................#
# def make_movies(name_of_movie,male_lead,year=None):
#     """Generates a dictionary with a movie, its male lead actor and the year it was made in"""
#     movie_list = {'name of movie': name_of_movie,'Leading actor': male_lead}
#     if year:
#         movie_list['year'] = year
#     return movie_list
#
# #Ask for movies infinitely
# while True:
#     name_movie = input(f"Movie: ")
#     male_lead = input(f"Lead Actor: ")
#     year_made = input(f"Release year: ")
#     new_movie_list = make_movies(name_movie, male_lead, year_made)
#     print(new_movie_list)
#     quit_program = input(f"Do you want to enter more movies (Y/N): ")
#     if quit_program == 'N':
#         break

# ...............................(6) messages.........................#
# text_messages = ['I am fine!', 'Driving now!', 'Call you later']
# def show_messages(text_messages):
#     """
#     Prints the messages
#     :param text_messages: List of messages
#     :return: Printed messages
#     """
#     for messages in text_messages:
#         print(f"The following messages are printed: {messages}")
#
#
# show_messages(text_messages)
# ...............................(7) updating the sent message list.........#
# def send_messages(text_messages, sent_messages):
#     """
#     Prints the messages
#     :param text_messages: List of messages
#     :return: Printed messages
#     """
#     # for messages in text_messages:
#     #     print(f"The following messages are printed: {messages}")
#     #     sent_messages.append(messages)
#     while text_messages:
#         messages = text_messages.pop()
#         print(f"Messages sent : {messages}")
#         sent_messages.append(messages)
#
#
# text_messages = ['I am fine!', 'Driving now!', 'Call you later']
# sent_messages = []
#
# send_messages(text_messages[:], sent_messages)
#
# print(text_messages)
# print(sent_messages)
# ...................................(8) Sandwiches........................#
# """Here we write a function that collects the items a person wants in his sandwich"""
#
# def make_sandwich(sandwich_name, *sandwich_items):
#     """
#     It takes all the items a user wants in his sandwich along with sandwich name
#     :param sandwich_name: Name of the sandwich
#     :param sandwich_items: Items user want in the sandwich
#     :return: Summary of the sandwich
#     """
#     print(f"\nThe user ordered {sandwich_name} sandwich with following items to be included: ")
#     for items in sandwich_items:
#         print(f"- {items}")
#
#
# make_sandwich('Cheese', 'Cheese','Bread', 'Tomatoes', 'Onions')
# .....................................(9) User_profile...........................#
# """In this example we write a function that biulds a user_profile taking various parameters"""
#
#
# def build_profile(first_name, last_name, **additional_info):
#     """
#     Takes information provided by user and summarizes the user profile
#     :param first_name: name
#     :param last_name: name
#     :param additional_info: additional data
#     :return: summarized data of the user input
#     """
#     additional_info['first name'] = first_name
#     additional_info['last name'] = last_name
#     return additional_info
#
#
# profile = build_profile('Shubham', 'Mishra', Age=24, Sex='Male')
# print(profile)
#

# # ...................................(10) Cars.............................#
# """ Another example on functions where we create a function that takes in various parameters
#     associated with cars"""
#
#
# def car_features(manufacturer, model_name, **additional_info):
#     """
#     Function takes in car manufacturer, model number and other arbitary key-value pairs
#     :param manufacturer: Maker
#     :param model_name: Car Name
#     :param additional_info: Other data
#     :return: Summary of the Car
#     """
#     additional_info['Manufacturer'] = manufacturer
#     additional_info['Model Name'] = model_name
#     return additional_info
#
#
# car = car_features('Audi', 'TT', Version='Sports', Year=2019)
# print(car)

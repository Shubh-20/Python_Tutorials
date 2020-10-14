# Functions are used for tasks that are repetative
# They help simplify the program

# .................Defining a function.....................
# def greet_user():#......Defination of a function
#     """Display a simple greeting.......doc string"""
#     print("Hello!")#........Operation of the function.........
#
# greet_user()#..........Calling the function..........

# .......Passing information to the function...........
# def greet_user(username):
#     """
# Displays a greeting with name
#     :param username:
#     """
#     print(f"Hello, {username.title()}!")
# greet_user('shubham')
#.......................POSITIONAL ARGUMENT..................
#arguments are matched with the parameters in the order they were given
# def describe_pet(animal_type,pet_name):
#     """Describes the animal and its name
#     :param animal_type, :param pet_name"""
#     print(f"I have a {animal_type.title()}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
#
# describe_pet('cat', 'melani')
# #We can call a function multiple times
# describe_pet('dog','schwung')

#***It is very important to check the order of the arguments in positional arguments***


#......................KEYWORD ARGUMENTS....................
#Its a key-value pair that is passed to the function
#This helps avoid the confusion with the order of passing the arguments

#The function remains the same
# def describe_pet(animal_type,pet_name):
#     """Describes the animal and its name
#     :param animal_type, :param pet_name"""
#     print(f"I have a {animal_type.title()}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# #But while calling that function we use a key value pair
# describe_pet(pet_name='Melani',animal_type='Cat')

#........................Default Values.......................#
# def describe_pet(pet_name, animal_type = 'dog'):
#     """Describes the animal and its name
#     :param animal_type, :param pet_name"""
#     print(f"I have a {animal_type.title()}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# #But while calling that function we use a key value pair
# describe_pet(pet_name='Marcus')

#........................Return Values.......................#
#The return statement takes a value from inside a function and send it back to the line that called the function
# def neatly_formtatted_name(first_name,last_name):
#     """This function returns neatly formatted name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = neatly_formtatted_name('Shubham','mishra')
# print(musician)

#Making an Argument Optional
# def neatly_formtatted_name(first_name, last_name, middle_name = ''):
#     """This function returns neatly formatted name"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = neatly_formtatted_name('shubham','mishra')
# print(musician)
#........................Returning a dictionary.....................#
# def build_a_person(first_name, last_name, age = None, sex = None):
#     """Describes a person with the given input data in a form of Dictionary"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     if sex:
#         person['sex'] = sex
#     return person
#
#
# musician = build_a_person('Rajesh','Khanna',45,'Male')
# print(musician)

#.......................Using a function with while loop...............#
# def neatly_formtatted_name(first_name,last_name):
#      """This function returns neatly formatted name"""
#      full_name = f"{first_name} {last_name}"
#      return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name")
#     f_name = input('First: ')
#     l_name = input('Last: ')
#     quit_program = input('Do you want to quit (Y/N): ')
#     if quit_program == 'Y':
#         break
#
#     formatted_name = neatly_formtatted_name(f_name,l_name)
#     print(f"\nHello, {formatted_name}!")

#...........................Passing a List to a function................#
#When we pass a list to a function, the function has all the acess to the contents in the list
# We have a list of users and we want to greet all the users individually so the code for that can be like this
# def greet_user(names):
#     """Print a simple message for all users in list"""
#     for name in names:
#         message = f"Hello, {name.title()}!"
#         print(message)
#
#
# usernames = ['raj','zuned','shubham']
# greet_user(usernames)

#.........................Modifying a List in a function...................#
""" A company creates a 3d printed model of designs that user submits, designs needed to be made
    are stored in one list and once designed they are moved into another list"""

# # Start with some designs that are needed to be printed
# unprinted_designs = ['phone case', 'robot pendent', 'plastic frame']
# completed_models = []
#
# # Simulate Printing each design, until none are left
# # Move each design to completed_models after printing
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing Model: {current_design}")
#     completed_models.append(current_design)
#
# # Display all completed models
# print('\nThe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model)
#................................ReStructured Code...............................#
# """ The above code can be restructured as two different functions, one which takes care of printing
#     and the second that shows what models have been printed"""
#
# def printing_models(unprinted_models, completed_models):
#     """
#     Simulate that the unprinted models are being printed
#
#     :param unprinted_models: List of Models that aren't printed
#     :param completed_models: List of Models that has been printed
#     :return: List of a models in completed list
#     """
#     while unprinted_models:
#         current_design = unprinted_models.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """
#     Show which models have been printed already
#     :param completed_models: List of models that have been printed
#     :return: A list that need to be printed
#     """
#     print('\nThe following models have been printed:')
#     for complete_models in completed_models:
#         print(complete_models)
#
#
# unprinted_designs = ['Car', 'Toy', 'Phone Cover']
# completed_list = []
#
# printing_models(unprinted_designs, completed_list)
# show_completed_models(completed_list)
#  """To avoid modification of the original list, a copy of list is given to the function,
#     in case if we wanted to save the list of unprinted_models we could use the command as
#     printing_models(unprinted_designs[:], completed_list) """

#..................................Passing Arbitary Numbers of Arguments...............#
# """Some times its not possible to know the number of arguments that will be needed to pass in a function
#     at such times we use the ability of python to pass arbitary number of arguments in a function"""
#
# def make_pizza(*toppings):
#     '''
#     Prints the list of toppings that have been requested
#     :param toppings: pizza toppings requested from user
#     :return: list of toppings
#     '''
#     print(f"\nMaking Pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_pizza('pepparoni', 'olives', 'mushrooms')

#..................................Mixing positional and Arbitary.....................#
#
# def make_pizza(size, *toppings):
#     """
#     Summarize the pizza we are about to make.
#     :param size: size of the pizza
#     :param toppings: toppings requested by the user
#     :return: summary of the pizza requested
#     """
#     print(f"\nMaking a pizza of {size}-inch with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza(6, 'mushroom', 'pepporoni', 'olives', 'chilli')

#...............................Using Arbitary Keywords argument....................#
# def build_profile(first, last, **user_info):
#     '''
#     Build a dictionary containing everything we know about the user
#     :param first: first name
#     :param last: last name
#     :param user_info: other details
#     :return: complete user details
#     '''
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile('Shubham', 'Mishra', location='germany', field='Electronics')
# print(user_profile)

#..................................Storing Function in Modules.........................#

#Counting with while loop
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


#Letting the user choose whn to quit
#prompt = "\nTell me something and I will repeat it back for you: "
#prompt += "\nEnter quit to end the program! "

# message = " "
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#...........................Using a Flag....................................
#If we have multiple conditions to be checked we use a flag concept
# active = True #sets the flag condition to true
# while active: #checking the conditions in while loop
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#...........................Using Break in while loop........................
# prompt = "\nPlease Enter the name of the City you have visited: "
# prompt += "\nType quit to finish."
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")
#...........................Using continue in a while loop...................
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)
#.........................While loop with lists and Dictionaries...............
#We have a list of unverified users for a websites and after verifying move them to the verified users
#Start with a list of users that are yet to be verified
#And an empty list to hold confirmed users
#
# unconfirmed_users = ['alice','eve','ryan','julie']
# confirmed_users = []

#Verify each user until there are no more unconfirmed users
# Move each verified users into the list of confirmed users
#
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_users.title()}")
#     confirmed_users.append(current_users)

#Display all verified users
# print("\nThe following users have been verified: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


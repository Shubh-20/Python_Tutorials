#Lists is a collection of items in certain order
bicycles = ['trek','cannondale','redline','specialized']
#print(bicycles)

#Accessing items in the list
#print(bicycles[0].title())
#Indexing starts at 0 not at 1
#Using a element from the list and printing a message based on it
message = f"My first bicycle was a {bicycles[0].title()}"
#print(message)
My_friends = ['Utshav','Zuned','Akash','David']
# print(My_friends[0].capitalize(),f"is one of my oldest and my best friend."
#       ,My_friends[-1].capitalize(),f"has been a good friend to since my college times")
#Changing Adding and removing elements
#Modifying elements in list
motorcycles = ['Suzuki','Honda','Yamaha','BMW']
#print(motorcycles)
motorcycles[0] = 'Ducati'
#print(motorcycles)
#Adding Elements to the end of list
motorcycles.append('Volkswagen')
#print(motorcycles)
#Creating an empty list and then appending items to it
Cars = []
Cars.append('BMW')
Cars.append('Audi')
Cars.append('VW')
# print(Cars)
#Inserting elements using the insert command
Cars.insert(2,'Maruti')
#Removing elements using the del command
del Cars[2]
#Removing elements using pop method
#pop method is used to remove an item from the list and still make it available to perform operations

#print(motorcycles)
last_owned_bike = motorcycles.pop(1)
# print(f"The last bike that I owned was a",last_owned_bike)
# print(motorcycles)
#Removing elements from a list using the "remove" command

motorcycles.remove('Ducati')
#print(motorcycles)


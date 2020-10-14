# """ First Method to importing, Importing the whole module and then using '.' operator"""
# from Pizza
#
# Pizza.make_pizza(16, 'Olives')
# Pizza.make_pizza(12, 'Mushrooms', 'Olives', 'Pepporoni')
#
# """ Second method is to use 'from' this 'import' that format"""
#
# from Pizza import make_pizza
#
# make_pizza(16, 'Olives')
# make_pizza(12, 'Mushrooms', 'Olives', 'Pepporoni')
#
# """ Third method is to use an alias for the function"""
#
# from Pizza import make_pizza as mp
#
# mp(16, 'Olives')
# mp(12, 'Mushrooms', 'Olives', 'Pepporoni')

# """ Using an alias for a module"""
# import Pizza as P
#
# P.make_pizza(16, 'Olives')
# P.make_pizza(12, 'Mushrooms', 'Olives', 'Pepporoni')
#
# """ Importing all functions of a Module """
#
# from Pizza import *
#
# make_pizza(16, 'Olives')
#  make_pizza(12, 'Mushrooms', 'Olives', 'Pepporoni')
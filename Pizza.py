def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    :param size: size of the pizza
    :param toppings: toppings requested by the user
    :return: summary of the pizza requested
    """
    print(f"\nMaking a pizza of {size}-inch with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")



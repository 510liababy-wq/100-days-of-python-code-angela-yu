from coffee_menu import MENU, resources

money = 0
machine_running = True



# TODO 4: When users choose a drink, check if there are enough resources to make it.
## If there aren't enough to make the drink, tell them we're out of that material

def check_resources(drink, machine_resources, menu_dictionary):
    """Check if there are enough of each material to make user's drink."""
    for resource in menu_dictionary[drink]["ingredients"]:
        if machine_resources[resource] < menu_dictionary[drink]["ingredients"][resource]:
            print(f"Sorry, there isn't enough {resource}")
            return False
    return True


# TODO 5: If there's enough resources to make the drink, ask the user to enter coins and calculate them
def calculate_coins():
    """Calculate the amount of money the user pays with and return it. """
    quarters = float(input("Enter quarters: ")) * 0.25
    dimes = float(input("Enter dimes: ")) * 0.10
    nickles = float(input("Enter nickles: ")) * 0.05
    pennies = float(input("Enter pennies: ")) * 0.01
    user_money = quarters + dimes + nickles + pennies
    return user_money


# TODO 6: Check if the user paid enough coins and refund if necessary. Add the cost of the drink to the Machine's Money

def transaction(amount_paid, drink):
    """Returns the amount of change if the user paid enough money to buy their drink."""
    if amount_paid < MENU[drink]["cost"]:
        return False
    else:
        return amount_paid - MENU[drink]["cost"]  # Amount of Change


# TODO 7: Subtract the amount of resources used from the amount of resources in the machine. GIve user their drink.
def make_coffee(coffee_menu, drink, machine_resources):
    """Deduct the amount of resources needed for the coffee"""
    for resource in coffee_menu[drink]["ingredients"]:
        machine_resources[resource] -= coffee_menu[drink]["ingredients"][resource]



while machine_running:

    # TODO 1: Ask the user what they would like to order
    user_order = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2: Make "off" function to turn off (break/quit()) the code
    if user_order == "off":
        machine_running = False

    # TODO 3: Create report function to print the current resources
    elif user_order == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money}")

    else:
        resources_available  = check_resources(user_order, resources, MENU)

        if resources_available:
            print("Please insert coins ")
            change = transaction(calculate_coins(), user_order)
            if change == False:
                print("Sorry that's not enough money! Money refunded...")
            else:
                print(f"Here is your change ${change:.2f}")
                make_coffee(MENU,user_order,resources)
                print(f"Here is your {user_order} ☕️. Enjoy! ")
                money += MENU[user_order]["cost"]



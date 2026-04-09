from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
cash_register  = MoneyMachine()
machine_menu = Menu()

machine_running  = True

while machine_running:
    user_choice = input("What would you like? (espresso/latte/cappuccino/): ")

    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        coffee_machine.report()
        cash_register.report()
    else:
        drink = machine_menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(drink) and cash_register.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)

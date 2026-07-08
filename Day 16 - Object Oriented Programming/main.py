from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
my_menu = Menu()
my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()


while is_machine_on:
    
    user_choice = input(f"What do you want bruh {my_menu.get_items()}: ").lower()

    if user_choice == "off":
        print("Turning coffee machine off")
        is_machine_on = False

    elif user_choice == "report":
        my_coffee_machine.report()
        my_money_machine.report()
        
    else: 
        
        drink = my_menu.find_drink(user_choice)
        if drink is not None:
            if my_coffee_machine.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
                my_coffee_machine.make_coffee(drink)
        else:
            print('tf cuh')


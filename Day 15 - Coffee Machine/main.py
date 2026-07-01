MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money" : 0 #added money to make reports easier
}

print(MENU["cappuccino"]["ingredients"])
is_machine_on = True
def report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")


def resource_update(user_choice):
    for item in MENU.keys(): # going through each item needed for that coffee
        if user_choice == item: #trying to match the user choice with key item in the menu
                for i in MENU[item]["ingredients"]:
                    for resource in resources.keys():
                        




def coffee_machine(user_choice):
    if user_choice == "report":
        report()
    elif user_choice == "cappuccino":
        pass



while is_machine_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    resource_update(user_choice)









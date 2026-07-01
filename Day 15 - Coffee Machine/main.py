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

is_machine_on = True
def report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")

report()


while is_machine_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino):")





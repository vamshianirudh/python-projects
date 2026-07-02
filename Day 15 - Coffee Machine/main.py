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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

print(MENU["cappuccino"]["ingredients"])
is_machine_on = True
def report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")


def resource_update(user_choice):
    for ingredient in MENU[user_choice]["ingredients"]: # goes into ingredients of the user_choice for comparison
        resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]

    resources["money"] += MENU[user_choice]["cost"] #need to update the cost only once, for loop will increment the cost for each ingredient






def coffee_machine(user_choice):
    if user_choice == "report":
        report()
    elif user_choice == "cappuccino":
        pass



while is_machine_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    resource_update(user_choice)

    report()









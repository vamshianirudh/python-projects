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

is_machine_on = True

def report():
    for resource in resources:
        # Formats the print slightly nicer for readability
        if resource in ["water", "milk"]:
            print(f"{resource.title()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.title()}: {resources[resource]}g")
        else:
            print(f"{resource.title()}: ${resources[resource]:.2f}")


def resource_update(user_choice):
    """Checks the resources and updates it"""
    drink_ingredients = MENU[user_choice]["ingredients"]
    
    # 1. First, check if ALL ingredients are available
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources.get(ingredient, 0):
            print(f"Sorry there is not enough {ingredient}")
            return False  # Return False to tell coffee_machine to cancel the order

    # 2. Process coin entry and payment validation
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    
    cost = MENU[user_choice]["cost"]
    
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
        
    # 3. Handle change if they overpaid
    change = round(total - cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")

    # 4. If ingredients and money are good, deduct resources and update money ONCE
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
        
    resources["money"] += cost
    print(f"Here is your {user_choice} ☕. Enjoy!")
    return True


def coffee_machine(user_choice):
    global is_machine_on
    if user_choice == "off":
        is_machine_on = False
        print("Turning off. Goodbye!")
    elif user_choice == "report":
        report()
    elif user_choice in MENU:
        resource_update(user_choice)
    else:
        print("Invalid selection.")


# Main Loop
while is_machine_on:
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    coffee_machine(user_choice)

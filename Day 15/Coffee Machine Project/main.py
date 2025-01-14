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
}

money = 0


def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if total >= MENU[coffee]["cost"]:
        change = total - MENU[coffee]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee} ☕ Enjoy!")
        global money
        money += MENU[coffee]["cost"]
        # Deduct resources
        for item in MENU[coffee]["ingredients"]:
            resources[item] -= MENU[coffee]["ingredients"][item]
    else:
        print("Sorry, that's not enough money. Money refunded.")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee == "off":
        print("Turning off the machine. Goodbye!")
        break
    elif coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:.2f}")
    elif coffee in MENU:
        if is_resource_sufficient(MENU[coffee]["ingredients"]):
            coins()
    else:
        print("Invalid option. Please choose espresso, latte, or cappuccino.")

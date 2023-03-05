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
profit = 0

is_on = True

def resources_suff(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return 
    return True


print(MENU)


def process_coins():
    print("Insert coins")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money")
        return False


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"heres your {drink_name} enjoy")


while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice]
        if resources_suff(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])

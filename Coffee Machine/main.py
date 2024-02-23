from coffeMachine import MENU, resources
from art import logo
import os


profit = 0


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def is_enough_resouces(order_ingredients):
    """Check wether ther are enough resouces to make the coffee or not"""
    for item in order_ingredients:
        if resources[item] <= order_ingredients[item]:
            print(f"Sorry there is not enought {item}")
            return False
    return True


def process_coins():
    print("Enter the coins: ")
    total = int(input("How many Quarters: ")) * 0.25
    total += int(input("How many Dimes: ")) * 0.1
    total += int(input("How many Nickels: ")) * 0.05
    total += int(input("How many Pennies: ")) * 0.01

    return total


def is_payment_successful(payment, drink_cost):
    """Check wether the payment is enought to make the coffee or not"""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is your change of ${change}")
        global profit
        profit += payment
        return True
    else:
        print("Sorry there was not enough money. Money Refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    """checks the ingredient and the drink name and then makes the coffee"""
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]

    print(f"Here's your {drink_name} ENJOY <3 ")


clear_screen()
print(logo)

machine_is_on = True

while machine_is_on:
    coffee_choice = input("Enter the coffee Espresso/Latte/Cappuccino: ").lower()
    if coffee_choice == "off":
        machine_is_on = False
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {resources}")
    else:
        drink = MENU[coffee_choice]
        if is_enough_resouces(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(coffee_choice, drink["ingredients"])

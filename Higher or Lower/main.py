# random account a and b form the data
import random
from data import data
from art import logo, vs
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def check_answer(guess, a_followers, b_followers):
    """Checks the followers of A against B"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def formatData(account):
    """Formats the data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description} from {account_country}"


def playGame():

    print(logo)
    score = 0
    should_continue = True

    while should_continue:
        account_A = random.choice(data)
        account_B = random.choice(data)

        print(f"Compare A: {formatData(account_A)}")
        print(vs)
        print(f"Aganist B: {formatData(account_B)}")

        a_followers = account_A["follower_count"]
        b_followers = account_B["follower_count"]

        guess = input("Guess the Highest Followers 'A' or 'B': ").lower()

        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You are right. Current Score = {score}")
        else:
            should_continue = False
            print(f"You are wrong, Final Score = {score}")

    userInput = input("Press Y to play Again or N to exit ")
    if userInput == "y":
        clear_screen()
        playGame()
    else:
        print("GoodBye")
        exit(0)


playGame()

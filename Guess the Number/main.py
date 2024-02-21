import random
import os
from art import logo

# GLOBAL VARIABLE
EASY_LEVEL = 10
HARD_LEVEL = 5


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def checkAnswer(guess, answer, tries):
    """Check the guess against the"""
    if guess == answer:
        print(f"You have guessed Right 💯\nAnswer = {answer}")
    elif guess < answer:
        print("Too Low Try again📉")
        return tries - 1
    elif guess > answer:
        print("Too High Try again📈")
        return tries - 1


def setDifficulty(mode):
    """Sets the difficulty of the game"""
    if mode == 1:
        return EASY_LEVEL
    elif mode == 2:
        return HARD_LEVEL
    else:
        print("Provide Valid Input❌❌")


def game():
    """Initialze the game itself"""
    print(logo)
    mode = int(input("Select the mode of difficulty\nEasy(1)\nHard(2) = "))
    answer = random.randrange(0, 101, 1)

    guess = 0
    tries = setDifficulty(mode)
    print(f"You have got {tries} GOOD LUCK")
    # print(tries)

    while guess != answer:
        guess = int(input("Guess the Number = "))
        tries = checkAnswer(guess, answer, tries)
        print(f"You left = {tries}")
        if tries == 0:
            print(f"You Lose the Answer = {answer}")
            break

    userInput = input("Press 'y' to play again or 'n' to exit: ")
    if userInput == "y":
        clear_screen()
        game()
    elif userInput == "n":
        print("Thank You")
        exit(0)


game()

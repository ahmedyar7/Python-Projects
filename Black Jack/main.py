import random
import os
from art import logo


def clear_screen():
    """Used to clear the screen"""
    os.system("cls" if os.name == "nt" else "clear")


def dealCard():
    """Picking random number from the cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculateScore(cards):
    "Calculate the score of randomized card"
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(userScore, computerScore):
    """Compare the user and the computer scores"""
    if userScore == computerScore:
        return "DRAW"
    elif computerScore == 0:
        return "YOU LOSE COMPUTER WIN"
    elif userScore == 0:
        return "YOU WIN COMPUTER LOSE"
    elif userScore > 21:
        return "YOU LOSE"
    elif computerScore > 21:
        return "YOU WIN"
    else:
        return "YOU WIN"


def playGame():

    print(logo)
    user_cards = []
    computer_cards = []
    gameEnd = False

    for _ in range(2):
        user_cards.append(dealCard())
        computer_cards.append(dealCard())

    while not gameEnd:

        userScore = calculateScore(user_cards)
        computerScore = calculateScore(computer_cards)

        print(f" USER CARD = {user_cards} : USER SCORE = {userScore}\n")
        print(
            f" COMPUTER FIRST CARD = {computer_cards[0]} : COMPUTER SCORE = {computerScore}\n"
        )

        if userScore == 0 or computer_cards == 0 or userScore > 21:
            gameEnd = True
        else:
            shouldContinue = input("Do you want to draw another Card 'y' or 'n': ")
            if shouldContinue == "y":
                user_cards.append(dealCard())
            else:
                gameEnd = True

        while computerScore < 17 and computerScore != 0:
            computer_cards.append(dealCard())
            computerScore = calculateScore(computer_cards)

    print(f"USER FINAL HAND = {user_cards} : USER FINAL SCORE = {userScore}\n")
    print(
        f"COMPUTER FINAL HAND = {computer_cards} : COMPUTER FINAL SCORE = {computerScore}\n"
    )
    print(compare(userScore, computerScore))


userInput = input("Do You want to play game of black Jack type 'y' or 'n': ")
if userInput == "y":
    clear_screen()
    playGame()
else:
    print("BYE")
    exit(0)

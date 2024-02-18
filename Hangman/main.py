import random
from wordList import wordList
from hangmanart import logo


print(logo)
randomWord = random.choice(wordList)
wordLength = len(randomWord)
gameEnd = False
lives = 5


# Creating Empty list:
display = []
for _ in range(wordLength):
    display += "_"

# Condition for the while loop

while not gameEnd:
    # looping through the string
    chosenLetter = input("Gussed a letter: ").lower()
    for i in range(wordLength):
        letter = randomWord[i]
        if letter == chosenLetter:
            display[i] = letter
            print(display)

    # Losing Condtion
    if chosenLetter not in randomWord:  # NOTE: loop end win/lose
        lives -= 1
        print(f"You guessed the wrong letter {lives} remaining")
    if lives == 0:
        gameEnd = True
        print("You Lose!")
    # Winning Condition:
    if "_" not in display:
        gameEnd = True
        print("You Win!")

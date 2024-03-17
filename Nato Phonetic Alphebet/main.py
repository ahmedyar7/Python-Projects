import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

game_is_on = True

while game_is_on:

    user_input = input("Enter the Word: ").upper()

    final_list = [phonetic_dict[letters] for letters in user_input]
    print(final_list)

    player_input = input("Do you want to continue, Yes or No: ").upper()

    if player_input == "NO":
        game_is_on = False
        print("Thank You ❤ ^ ❤")

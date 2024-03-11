# TODO: open ready to sent file and then write new letters

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)


with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    print(letter_content)

    for names in names:
        stripped_names = names.strip()

        new_letters = letter_content.replace(PLACEHOLDER, stripped_names)

        with open(
            f"Output/ReadyToSend/new_letters_{stripped_names}.txt", mode="w"
        ) as ready_to_send:
            ready_to_send.write(new_letters)

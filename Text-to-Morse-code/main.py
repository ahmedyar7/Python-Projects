import re
import time
import winsound


MORSE_CODE: dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/",
}

MORSE_CODE_REVERSED: dict[str, str] = {
    values: key for key, values in MORSE_CODE.items()
}

# Constants for Sound
FREQUENCY = 800
DOT_DURATION = 100
DASH_DURATION = 300
LETTER_PAUSE = 0.3
WORD_PAUSE = 0.7


def play_morse_sound(morse: str) -> str:
    """This would play morse sound according to the conventions

    Args:
        morse (morse): Actual morse code
    """

    for symbols in morse:
        if symbols == ".":
            winsound.Beep(FREQUENCY, DOT_DURATION)

        elif symbols == "-":
            winsound.Beep(FREQUENCY, DASH_DURATION)

        elif symbols == " ":
            time.sleep(LETTER_PAUSE)

        elif symbols == "/":
            time.sleep(WORD_PAUSE)

        else:
            print(f"Unknown Morse Symbol {symbols}")


def text_to_morse(text: str) -> str:
    """This function converts English text to morse code

    Args:
        text (str): English Text

    Returns:
        str: Morse code Equvilent
    """

    # Normalize spaces
    text = re.sub(r"\s+", " ", text.upper().strip())

    morse = "".join(MORSE_CODE.get(char, "?") for char in text)
    return morse


def morse_to_text(morse: str) -> str:
    """This would convert morse code into string
        and subsequently plays the sound

    Args:
        morse (str): Morse code

    Returns:
        str: English text
    """

    words = morse.strip().split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()

        for letter in letters:
            decoded_word = "".join(MORSE_CODE_REVERSED.get(letter, "?"))
            decoded_words.append(decoded_word)

    return " ".join(decoded_words)


def main():
    """
    Main function to handle user input and process Morse Code conversion.
    """
    while True:
        choice = input(
            "\nChoose:\n1 - Text to Morse\n2 - Morse to Text\n3 - Exit\nEnter choice: "
        )

        if choice == "1":
            text = input("\nEnter text: ")
            morse_code = text_to_morse(text)
            print("\nMorse Code:", morse_code)
            play_morse_sound(morse_code)

        elif choice == "2":
            morse = input("\nEnter Morse Code (use '/' for spaces between words): ")
            text = morse_to_text(morse)
            print("\nDecoded Text:", text)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

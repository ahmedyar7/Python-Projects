import re

MORSE_CODE = {
    "A": ".-",
    "N": "-.",
    "B": "-...",
    "O": "---",
    "C": "-.-.",
    "P": ".--.",
    "D": "-..",
    "Q": "--.-",
    "E": ".",
    "R": ".-.",
    "F": "..-.",
    "S": "...",
    "G": "--.",
    "T": "-",
    "H": "....",
    "U": "..-",
    "I": "..",
    "V": "...-",
    "J": ".---",
    "W": ".--",
    "K": "-.-",
    "X": "-..-",
    "L": ".-..",
    "Y": "-.--",
    "M": "--",
    "Z": "--..",
}

MORSE_CODE_REVERSED = {values: key for key, values in MORSE_CODE.items()}

# Text for morse code
text = input("Enter a Key: ").upper()
text = re.sub(r"\s+", "", text)


def text_to_morse(key: str) -> str:
    output = []
    for char in key:
        if char in MORSE_CODE:
            output.append(MORSE_CODE[char])
        else:
            print(f"Key = {char} was not found")

    # converting array element to string
    result = " ".join(map(str, output))
    return result


morse_code = text_to_morse(key=text)


morse_word = morse_code.split("   ")


def morse_to_text(morse_word: str) -> str:
    decoded_words = []

    for words in morse_word:
        morse_letters = words.split(" ")
        decoded_letters = []

        for letters in morse_letters:
            if letters in MORSE_CODE_REVERSED:
                decoded_letters.append(MORSE_CODE_REVERSED[letters])
            else:
                print(f"The morse code was not found {letters}")

        decoded_words.append("".join(decoded_letters))

    morse_decoded = " ".join(decoded_words)
    return morse_decoded

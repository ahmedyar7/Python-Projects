# TODO: Figure out the morse code equvilent of ABC then store them in a dictionary
# TODO: Figure out a way to convert text to morse code
# TODO: Figure out a way to convert morse code back to text


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
print(MORSE_CODE_REVERSED)

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
    result = "".join(map(str, output))
    return result


morse = input("Enter a morse: ").upper()
morse = re.sub(r"\s+", "", morse)


def morse_to_text(key: str) -> str:
    output = []
    for char in key:
        if char in MORSE_CODE_REVERSED:
            output.append(MORSE_CODE_REVERSED[char])
        else:
            print(f"Key = {char} was not found")

    # converting array element to string
    result = "".join(map(str, output))
    return result


morse_2_text = morse_to_text(key=morse)
print(f"Morse to Text = {morse_2_text}")

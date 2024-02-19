from alphabets import alphabets
from art import logo


print(logo)

mayContinue = True

while mayContinue:
    direction = input("Type encode to encrypt or decode to decrypt: ").lower()
    if direction != "encode" or direction != "decode":
        print("Please Enter Valid Input")
        exit(0)
    text = input("Enter the text: ").lower()
    shift = int(input("Enter Shift Amount: "))
    shift = shift % 26  # if user give shift number greater than the 26

    # Encoding Function:
    def encrypt(text, shiftAmount):
        codedText = ""
        for char in text:
            if char in text:
                position = alphabets.index(char)
                newPosition = position + shiftAmount
                codedText += alphabets[newPosition]
        print(codedText)

    # Decoding text:
    def decrypt(cipherText, shiftAmount):
        decodedText = ""
        for char in cipherText:
            if char in cipherText:
                position = alphabets.index(char)
                newPosition = position - shiftAmount
                decodedText += alphabets[newPosition]
        print(decodedText)

    if direction == "encode":
        encrypt(text=text, shiftAmount=shift)
    elif direction == "decode":
        decrypt(cipherText=text, shiftAmount=shift)

    # Condition for breaking while
    userInput = input("Do You want to Continue YES/NO: ").lower()
    if userInput == "no":
        mayContinue = False
        print("GoodBye <3")

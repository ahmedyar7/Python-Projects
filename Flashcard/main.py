from tkinter import *

# TODO Make the buttons known and the unknown and give the there images

BACKGROUND_COLOR = "#55E628"

# * ----------------------------------------- USER INTEFACE --------------------------------------- #


window = Tk()
window.title("FlashCard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(height=526, width=800)

card_front_image = PhotoImage(file="Flashcard/images/card_front.png")
card_back_image = PhotoImage(file="Flashcard/images/card_back.png")

canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="title")
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="word")

canvas.grid(row=0, column=0, columnspan=2)

# * ------------------- BUTTONS ------------------- #

right_image = PhotoImage(file="Flashcard/images/right.png")
wrong_image = PhotoImage(file="Flashcard/images/wrong.png")

known_button = Button(image=right_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=0)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)


window.mainloop()

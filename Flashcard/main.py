from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#79DD5B"


data = pandas.read_csv("Flashcard/data/french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

# * -------------------- NEXT CARD ---------------- #


def next_card():
    """This give funtionality to the buttons to display the next card"""
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_image, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)


# * --------------------- FLIP CARD ----------------------- #


def flip_card():
    """This function would flip the card after the 3 seconds to show the English translation of the word"""

    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])

    canvas.itemconfig(card_image, image=card_back_image)


# * ---------------------- KNOWN WORDS --------------- #


def is_known():
    """This function would work when we click the right button or the known button"""

    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)

    data.to_csv("Flashcard/data/words_to_learn.csv")

    next_card()


# * ----------------------------------------- USER INTEFACE --------------------------------------- #


window = Tk()
window.title("FlashCard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)

card_front_image = PhotoImage(file="Flashcard/images/card_front.png")
card_back_image = PhotoImage(file="Flashcard/images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="title")
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="word")

canvas.grid(row=0, column=0, columnspan=2)

# * ------------------- BUTTONS ------------------- #

right_image = PhotoImage(file="Flashcard/images/right.png")
wrong_image = PhotoImage(file="Flashcard/images/wrong.png")

known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=0)

unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()

window.mainloop()

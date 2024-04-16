from tkinter import *


class UserInterface:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Workout Tracker")

        self.title_label = Label(text="Workout Tracker")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10)

        self.entry_tag = Entry()
        self.entry_tag.grid(row=1, column=0, columnspan=2, padx=10)

        self.add_button = Button(text="Add")
        self.add_button.grid(row=2, column=0, pady=10, padx=10)

        self.visit_button = Button(text="Visit")
        self.visit_button.grid(row=2, column=1, columnspan=1, pady=10, padx=10)

        self.window.mainloop()


ui = UserInterface()

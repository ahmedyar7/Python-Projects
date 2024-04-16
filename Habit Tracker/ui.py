from tkinter import *

# Define a constant for theme color
THEME_COLOR = "#F1F5F5"


class UserInterface:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        self.window.title("Habit Tracker")

        # Configure window size and background color
        self.window.geometry("250x200")
        self.window.config(bg=THEME_COLOR)

        # Create the habit tracker label
        self.habit_tracker_label = Label(
            self.window,
            text="Habit Tracker",
            bg=THEME_COLOR,
            font=("Arial", 16, "bold"),  # Simple and clear font
        )
        self.habit_tracker_label.pack(pady=20)  # Pack for vertical spacing

        # Create a frame for habit and entry
        self.habit_frame = Frame(self.window, bg=THEME_COLOR)
        self.habit_frame.pack()

        # Create the habit label
        self.habit_label = Label(
            self.habit_frame, text="Reading", bg=THEME_COLOR, font=("Arial", 12)
        )
        self.habit_label.grid(row=0, column=0, sticky=W)  # Align left

        # Create the habit entry field
        self.habit_entry = Entry(self.habit_frame)
        self.habit_entry.grid(row=0, column=1, padx=5, pady=5)  # Add padding

        # Create the buttons in a frame
        self.button_frame = Frame(self.window, bg=THEME_COLOR)
        self.button_frame.pack()

        # Create the "Enter" button
        self.habit_enter_button = Button(self.button_frame, text="Enter", width=8)
        self.habit_enter_button.grid(row=0, column=0, padx=5, pady=5)  # Add padding

        # Create the "Visit" button
        self.habit_visit_button = Button(self.button_frame, text="Visit", width=8)
        self.habit_visit_button.grid(row=0, column=1, padx=5, pady=5)  # Add padding

        # Start the main event loop
        self.window.mainloop()


# Create the user interface instance
ui = UserInterface()

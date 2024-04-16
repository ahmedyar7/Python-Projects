from tkinter import *
from tracker import HabitTracker
from os import getenv
from dotenv import find_dotenv, load_dotenv
import webbrowser

# Define a constant for theme color
THEME_COLOR = "#F1F5F5"
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

URL = getenv("URL")
# print(URL)


TOKEN = getenv("TOKEN")

USERNAME = getenv("USER_NAME")
GRAPH_ID = getenv("GRAPH_ID")
HEADERS = {"X-USER-TOKEN": TOKEN}
API_ENDPOINT = "https://pixe.la/v1/users"

habit_tracker = HabitTracker(
    TOKEN=TOKEN,
    USERNAME=USERNAME,
    GRAPH_ID=GRAPH_ID,
    HEADERS=HEADERS,
    API_ENDPOINT=API_ENDPOINT,
)


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
            padx=10,  # Add horizontal padding
            pady=10,  # Add vertical padding
        )
        self.habit_tracker_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 10),
            sticky="ew",
        )  # Span 2 columns

        # Create the habit label
        self.habit_label = Label(
            self.window, text="Reading", bg=THEME_COLOR, font=("Arial", 12)
        )
        self.habit_label.grid(
            row=1,
            column=0,
            sticky=W,
            padx=(10, 0),
            pady=5,
        )  # Align left, add left padding

        # Create the habit entry field
        self.habit_entry = Entry(self.window)
        self.habit_entry.grid(
            row=1,
            column=1,
            padx=(0, 10),
            pady=5,
            sticky="ew",
        )  # Add right padding, align left

        def handle_button_click():
            self.value = self.habit_entry.get()  # Get the value from the entry field
            habit_tracker.update_pixel(amount=self.value)

        # Create the buttons

        self.habit_enter_button = Button(
            self.window,
            text="Enter",
            width=8,
            command=handle_button_click,
        )
        self.habit_enter_button.grid(
            row=2,
            column=0,
            padx=(10, 5),
            pady=5,
            sticky="ew",
        )  # Add left padding

        self.habit_visit_button = Button(
            self.window,
            text="Visit",
            width=8,
            command=visit_url,
        )
        self.habit_visit_button.grid(
            row=2,
            column=1,
            padx=(5, 10),
            pady=5,
            sticky="ew",
        )  # Add right padding

        # self.handle_button_click()

        # Start the main event loop
        self.window.mainloop()


def visit_url():
    """This will help you visit the url"""

    url = URL

    webbrowser.open_new(url=url)


# Update the pixel with the value


ui = UserInterface()


# Update the pixel with the value


# Create the user interface instance

# print(.habit_entry.get())

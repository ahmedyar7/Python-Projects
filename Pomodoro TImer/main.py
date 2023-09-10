from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET -------------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.configure(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ---------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.configure(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.configure(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.configure(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_mins = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, (count - 1))
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        check_label.configure(text=marks)


# ---------------------------- UI SETUP ------------------------------------------- #

# --- Screen setup ---:
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# --- Labels ---:
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


# --- Canvas setup ---:
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
# This read throught the file and create image
tomato_image = PhotoImage(file="tomato.png")
# this would create image from the file Variable
canvas.create_image(100, 112, image=tomato_image)
# this would create text
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


# --- Button Setup ---:
start_button = Button(
    text="Start", font=(FONT_NAME), highlightthickness=0, command=start_timer
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset", font=(FONT_NAME), highlightthickness=0, command=reset_timer
)
reset_button.grid(column=2, row=2)

window.mainloop()

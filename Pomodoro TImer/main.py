from tkinter import *
import math


## CONSTANTS


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

####################### TIMER RESET #########################


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks_label.config(text="")
    global reps
    reps = 0


################## Timer Mechanism #####################


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_min)

    elif reps % 2 == 0:
        count_down(short_break_min)
        timer_label.config(text="Break", fg=RED)

    else:
        count_down(work_sec)
        timer_label.config(text="Work")


################## COUNTDOWN MECHANISM: ###############


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += "✔"
        check_marks_label.config(text="Marks")


##################### User Interface #######################


window = Tk()

window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

## Setting up the title text
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

## Setting up the Image onto the screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
canvas.grid(column=1, row=1)

## Timer Text
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=("Cascadia Code", 35, "bold")
)

## Setting Up the Buttons
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


check_marks_label = Label(fg=GREEN, bg=YELLOW)

window.mainloop()

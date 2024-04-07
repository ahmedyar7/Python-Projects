from tkinter import *
import math

# * CONSTRAINTS:

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
# * ----------------------------- RESET MECHANISM -------------------------


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    global reps
    reps = 0


# * --------------------------- START TIMER ------------------------------
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    count_down(work_seconds)

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="Short Break", fg=RED)
    else:
        count_down(work_seconds)
        timer_label.config(text="Work", fg=GREEN)


# * -------------------------------- COUNTDOWN MECHANISMS ------------------------
def count_down(count):
    count_minutes = math.floor(round(count / 60))
    count_seconds = count % 60

    if int(count_seconds) < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
        check_mark_label.config(text=mark)


# * -------------------------------- USER INTERFACE -----------------------------

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro Timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

# * Label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

# * Buttons
start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# * Checked mark
check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)


window.mainloop()

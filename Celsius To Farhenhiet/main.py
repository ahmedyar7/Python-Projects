from tkinter import *


def c_into_f():
    celsius = float(celsius_input.get())
    forumla = (celsius * 9 / 5) + 32
    fahrenheit = forumla
    fah_result_label.config(text=f"{fahrenheit}")


window = Tk()


celsius_in_label = Label(text="Celsius")
celsius_in_label.grid(row=0, column=0)
celsius_input = Entry()
celsius_input.grid(row=0, column=1)


equal_to_label = Label(text="Is equal to")
equal_to_label.grid(row=1, column=0)


fah_result_label = Label(text="0")
fah_result_label.grid(row=1, column=1)


fah_label = Label(text="Farhenhiet")
fah_label.grid(row=1, column=2)

calc_button = Button(text="Convert", command=c_into_f)
calc_button.grid(row=2, column=1)


window.mainloop()

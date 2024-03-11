# TODO: Adding the score counter

from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()

img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)


data = pandas.read_csv("50_states.csv")
states_names = data.state.tolist()

correct_names = []

while len(correct_names) < 50:
    guessed_names = screen.textinput(
        title=f"50 States of USA {len(correct_names)}/50 ", prompt="Guess the next one?"
    ).title()

    if guessed_names in states_names:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guessed_names]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guessed_names)

print(len(correct_names))

screen.mainloop()

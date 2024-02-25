from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

user_input = screen.textinput(title="Enter the color", prompt="Place Your bet")

new_turtles = []
y_coordinates = [-70, -40, -10, 20, 50, 80]

for turtles_index in range(0, 6):
    turtles = Turtle(shape="turtle")
    turtles.color(colors[turtles_index])
    turtles.penup()
    turtles.goto(x=-230, y=y_coordinates[turtles_index])

    new_turtles.append(turtles)

game_is_on = False

if user_input:
    game_is_on = True

while game_is_on:

    for turtles_moves in new_turtles:
        random_movements = random.randint(0, 10)
        turtles_moves.forward(random_movements)

        if turtles_moves.xcor() > 230:
            game_is_on = False
            winner_color = turtles_moves.pencolor()

            if user_input == winner_color:
                print(f"You Have Won {winner_color} Wins The Race")
            else:
                print(f"You Have lost {winner_color} Wins The Race")

screen.mainloop()

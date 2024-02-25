# Turtle Movement Control with Keyboard Input

This Python script allows you to control a turtle using keyboard inputs. The turtle moves forward, backward, turns left, and turns right in response to specific key presses. Additionally, there's a function to clear the screen and reset the turtle to its initial position.

## Requirements

- Python 3.x
- Turtle module (usually comes pre-installed with Python)

## Usage

1. Clone or download the repository to your local machine.
2. Run the Python script `turtle_movement.py`.
3. The turtle window will appear, and you can control the turtle using the following keys:
    - **W**: Move the turtle forward
    - **S**: Move the turtle backward
    - **A**: Turn the turtle left
    - **D**: Turn the turtle right
    - **C**: Clear the screen and reset the turtle to its initial position

## Code Explanation

- `from turtle import Turtle, Screen`: Importing the necessary modules from the turtle library.
- `turtle = Turtle()`: Creating a turtle object.
- `screen = Screen()`: Creating a screen object.
- Movement functions:
  - `move_forward()`: Moves the turtle forward by 10 units.
  - `move_backward()`: Moves the turtle backward by 10 units.
  - `move_left()`: Turns the turtle left by 100 degrees.
  - `move_right()`: Turns the turtle right by 10 degrees.
  - `clear_screen()`: Clears the screen and resets the turtle to its initial position.
- `screen.listen()`: Allows the screen to listen for keyboard inputs.
- Key bindings:
  - `screen.onkeypress(key="w", fun=move_forward)`: Binds the "W" key to the `move_forward()` function.
  - `screen.onkeypress(key="s", fun=move_backward)`: Binds the "S" key to the `move_backward()` function.
  - `screen.onkeypress(key="a", fun=move_left)`: Binds the "A" key to the `move_left()` function.
  - `screen.onkeypress(key="d", fun=move_right)`: Binds the "D" key to the `move_right()` function.
  - `screen.onkeypress(key="c", fun=clear_screen)`: Binds the "C" key to the `clear_screen()` function.
- `screen.mainloop()`: Starts the event loop, allowing the program to listen for events (keyboard inputs) and respond accordingly.

Feel free to modify the code to suit your needs or integrate it into your projects.

## Author

- [Ahmed Yar](https://github.com/ahmedyar7)


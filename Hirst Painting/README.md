# Hirst Painting using Turtle

This Python script generates a series of dots using the Turtle graphics library. Each dot is randomly colored from a predefined color palette.

## Instructions
1. Make sure you have Python installed on your system.
2. Install the Turtle graphics library if you haven't already. You can install it using pip:
   ```
   pip install PythonTurtle
   ```
3. Create a Python file and copy the provided code into it.
4. Run the script.
5. Watch as dots appear on the screen, forming a pattern.

## How it Works
1. The script imports necessary modules: `Turtle`, `Screen`, and `colormode` from Turtle graphics library, and `random`.
2. `colormode(255)` is called to set the color mode to 255 (RGB mode).
3. A Turtle instance and a Screen instance are created.
4. The turtle's heading is set to 225 degrees, and it moves forward by 300 units, then resets its heading to 0.
5. The variable `num_of_dots` is set to 100, indicating the number of dots to be drawn.
6. A loop iterates from 1 to `num_of_dots`:
   - At each iteration, a dot with a random color from `color_pallet` is drawn using the `dot()` method of the turtle. The dot has a size of 20.
   - The turtle moves forward by 50 units.
   - If the current dot count is divisible by 10 (i.e., every 10 dots):
     - The turtle's heading is set to 90 degrees (upward).
     - The turtle moves forward by 50 units.
     - The turtle's heading is set to 180 degrees (left).
     - The turtle moves forward by 500 units (to reset the position).
     - The turtle's heading is set back to 0 degrees (right).
7. The `mainloop()` method of the screen keeps the window open until it is manually closed.

## Customization
- You can adjust the `num_of_dots` variable to change the number of dots generated.
- You can modify the color palette in the `color_pallet` list to use different colors for the dots.
- Experiment with different dot sizes and forward distances to create various patterns.

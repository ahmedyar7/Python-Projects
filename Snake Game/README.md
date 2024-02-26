# Snake Game 

This is a simple implementation of the classic Snake game using Python's Turtle module. The game consists of a snake that moves around the screen, eating food to grow longer. The goal is to avoid colliding with the walls or the snake's own body.

## Components:

### 1. `main.py`

- This is the main script that initializes the game environment, creates instances of the Snake, Food, and ScoreBoard classes, and handles the game loop.

### 2. `snake.py`

- Defines the Snake class responsible for controlling the snake's movement, extending the snake's length, and detecting collisions with itself.

### 3. `food.py`

- Contains the Food class that manages the appearance and position of the food on the screen.

### 4. `ScoreBoard.py`

- Implements the ScoreBoard class to keep track of the player's score and display game over messages.

## Usage:

1. Run `main.py` to start the game.
2. Use arrow keys (Up, Down, Left, Right) to control the snake's movement.
3. Eat food to increase your score.
4. Avoid collisions with walls or the snake's own body to continue playing.
5. When the game is over, the score and a game over message will be displayed.

## Dependencies:

- Python 3.x
- Turtle module

## Setup:

1. Clone the repository:

```bash
git clone https://github.com/ahmedyar7/Snake-Game.git

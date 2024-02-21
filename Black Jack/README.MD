# Simple Blackjack Game

This is a simple command-line Blackjack game implemented in Python.

## How to Play

1. Run the Python script `blackjack.py`.
2. You'll be prompted to play the game by typing 'y' or 'n'.
3. If you choose to play ('y'), the game will start.
4. You'll receive two cards, and the dealer (computer) will also receive two cards with one card face-up.
5. You can choose to draw additional cards or stop drawing ('n').
6. The dealer will then draw cards until their score is 17 or higher.
7. After both players have completed drawing cards, the winner is determined.
8. The game will then ask if you want to play again.

## Functionality

- Random card dealing
- Score calculation for both player and dealer
- Comparison of scores to determine the winner
- Ability to play multiple rounds

## How to Run

1. Ensure you have Python installed on your system.
2. Install the `art` library using `pip install art`.
3. Run the Python script `blackjack.py`.

## Clearing the Screen

- The game clears the screen before starting and after each round for better visibility.
- This feature works on both Windows and Unix-like systems.

## Notes

- The game uses a simple logic for scoring and comparison.
- This is a basic implementation of Blackjack and doesn't include advanced features like splitting, doubling down, or insurance.

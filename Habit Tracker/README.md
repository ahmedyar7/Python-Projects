# Habit Tracker

This repository contains code for a Habit Tracker application. The application is designed to track habits using the Pixela API.

## Installation

To use this application, you'll need to set up the following:

1. **Environment Variables**: Create a `.env` file in the root directory of the project and define the following environment variables:
   - `TOKEN`: Your Pixela API token.
   - `USER_NAME`: Your Pixela username.
   - `GRAPH_ID`: The ID of the graph to track habits.

2. **Python Dependencies**: Install the required Python dependencies using pip:
   ```bash
   pip install -r requirements.txt

## Code Structure

The code is structured into two main modules:

- **tracker.py**: This module contains the `HabitTracker` class, responsible for interacting with the Pixela API. It handles tasks such as creating users, creating graphs, creating pixels, updating pixels, and deleting pixels.

- **ui.py**: This module contains the `UserInterface` class, which defines the graphical user interface using Tkinter. It provides a simple interface for users to input habits and interact with the habit tracking functionality.

The `main.py` script imports these modules, sets up environment variables, instantiates the `HabitTracker` and `UserInterface` classes, and runs the application.

## Dependencies

The application relies on the following dependencies:

- `requests`: For making HTTP requests to the Pixela API.
- `tkinter`: For creating the graphical user interface.

These dependencies are specified in the `requirements.txt` file and can be installed using pip.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

.

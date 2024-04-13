# Quizzy App

Quizzy App is a simple quiz application built in Python using Tkinter for the graphical user interface (GUI). It allows users to take a quiz consisting of multiple-choice questions fetched from the Open Trivia Database API.

## Components

### `Question` Class

The `Question` class represents a single trivia question. It contains attributes for the question text and the correct answer.

### `QuizBrain` Class

The `QuizBrain` class manages the logic for the quiz. It keeps track of the current question, the score, and whether there are more questions remaining. It also provides methods to retrieve the next question and check the user's answer.

### `QuizInterface` Class

The `QuizInterface` class implements the graphical user interface using Tkinter. It sets up the window, canvas, labels, and buttons for the quiz. It also handles user interactions such as button clicks and updates the UI based on the quiz state.

### `question_data` Module

The `question_data` module contains a list of trivia questions fetched from the Open Trivia Database API. Each question is represented as a dictionary containing the question text and the correct answer.

### `requests` Module

The `requests` module is used to make HTTP requests to the Open Trivia Database API in order to fetch trivia questions. It sends a GET request with specified parameters such as the number of questions and the question type.

## Usage

1. Run the `quizzy.py` script to start the quiz application.
2. Answer the trivia questions by clicking the True or False buttons.
3. See your score at the end of the quiz.

## Dependencies

- Python 3.x
- Tkinter (Python GUI library)
- requests (Python HTTP library)

## Installation

1. Clone the repository:

- git clone https://github.com/ahmedyar7/Python-Projects/quizzy-app.git

3. Run the application:

- python main.py


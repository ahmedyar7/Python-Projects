# Quiz App


This is a simple quiz application where users can answer multiple-choice questions.

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Open a terminal and navigate to the directory where the code is located.
4. Run the following command:

    ```
    python quiz_app.py
    ```

5. Follow the prompts to answer each question.

## Features

- Multiple-choice questions with options.
- Keeps track of the user's score.
- Displays the final score at the end of the quiz.

## Files

- `quiz_app.py`: Main Python script to run the quiz application.
- `question_model.py`: Contains the Question class definition.
- `data.py`: Contains the question data in a list of dictionaries.
- `quiz_brain.py`: Contains the QuizBrain class definition for handling quiz logic.
- `art.py`: Contains the ASCII art for the logo.

## How it Works

1. The question data is loaded from `data.py`.
2. Each question is instantiated as a `Question` object using the `Question` class from `question_model.py`.
3. The quiz logic is handled by the `QuizBrain` class from `quiz_brain.py`.
4. The user interacts with the quiz through the terminal.
5. After answering all questions, the final score is displayed.

## Dependencies

- Python 3.x

## Contributors

- [Ahmed Yar](<https://github.com/ahmedyar7>)

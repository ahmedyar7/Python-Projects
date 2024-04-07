# Pomodoro Timer

This is a simple implementation of a Pomodoro Timer application using Python's `tkinter` library. The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Functionality

### Timer Settings
- **Work Time**: By default, the work time is set to 25 minutes.
- **Short Break Time**: By default, the short break time is set to 5 minutes.
- **Long Break Time**: By default, the long break time is set to 20 minutes.
- **Constraints**: These values are defined as constants in the code and can be adjusted as needed.

### Start Timer
- Clicking on the "START" button initiates the timer.
- The timer alternates between work sessions and breaks based on the Pomodoro Technique.
- After completing a work session or break, the next session type is displayed on the timer label.
- The countdown is displayed on a canvas using the format MM:SS.

### Reset Timer
- Clicking on the "RESET" button stops the current timer and resets it to the initial state.
- Any ongoing work or break session is cancelled, and the timer starts from the beginning.

### Check Marks
- After completing each work session, a check mark is displayed below the timer to track completed sessions.
- A check mark represents one completed work session.

## How to Use

1. Clone or download the repository.
2. Make sure you have Python installed on your system.
3. Navigate to the directory containing the `pomodoro_timer.py` file.
4. Run the script using the command `python pomodoro_timer.py`.
5. Click on the "START" button to begin the Pomodoro Timer.
6. Use the "RESET" button to stop and reset the timer if needed.

## Dependencies
- Python 3.x
- tkinter (usually included in standard Python distributions)

## Additional Notes
- You can customize the timer settings by modifying the constants defined in the code.
- Ensure the `Pomodoro Timer` directory contains the `tomato.png` image file for the tomato icon to display properly.

## Credits
- This implementation is inspired by the Pomodoro Technique developed by Francesco Cirillo.
- The code is written in Python using the `tkinter` library for GUI development.


# Password Manager

This is a simple password manager application built using Tkinter in Python. It allows users to generate random passwords and store them along with website and email information.

## Functionality

### Generate Random Password
- The "Generate" button allows users to generate a random password.
- The generated password consists of:
  - 5 random letters (both uppercase and lowercase)
  - 2 random digits
  - 2 random symbols from a predefined set of symbols.

### Save Password
- Users can input the website, email/username, and password into the corresponding entry fields.
- The "Add" button allows users to save the entered information into a data file named `data.txt`.
- Before saving, the application checks if both the website and password fields are filled. If any of them is empty, it shows an error message.
- After successful saving, it shows a confirmation message.

### User Interface
- The application has a simple user interface with fields for entering website, email/username, and password.
- It uses Tkinter for GUI components.
- It displays a logo using a `logo.png` file.
- Users can also generate a random password using the "Generate" button.

![Alt Text](/Password%20manager/randompass.png)



## How to Run
To run the application, execute the Python script `password_manager.py`.

```bash
python password_manager.py



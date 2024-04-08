from tkinter import *
from tkinter import messagebox
from random import *
import json


# * --------- CONSTANSTS ---------------- * #
my_email = "ahmedyar778@gmail.com"

# * ------------- GENERATE RANDOM PASSWORD --------------- * #


def generate_passoword():
    """This would generate random password after clicking the generte key"""

    letters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = "!@#$%^&*()_+-=`~<>/?;|"

    letters_list = list(letters)
    symbols_list = list(symbols)

    random_letters = sample(letters_list, 5)
    random_digits = str(sample(digits, 2))
    random_symbols = sample(symbols_list, 2)

    random_password = (
        "".join(random_letters) + "".join(random_digits) + "".join(random_symbols)
    )

    password_entry.insert(END, random_password)


# * ----------------------- SAVE PASSWORD ----------------------


def save():
    """Take the enteries and the store it into a data file"""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error", message="None of the feilds could remain empty"
        )
    else:
        # Error handling
        try:
            with open("Password Manager/data.json", mode="r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("Password Manager/data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # changing it with new data
            data.update(new_data)

            with open("Password Manager/data.json", mode="w") as data_file:
                # update the file with new data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# * ----------------------  User Interface  --------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# * --- Screen --- * #
canvas = Canvas(height=200, width=200)
password_logo = PhotoImage(file="Password Manager/logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(row=0, column=1)

# * --- Labels --- * #
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# * ---- Enteries ---- * #
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, my_email)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# * ----- Buttons ------ * #

generate_pass_button = Button(text="Generate", command=generate_passoword)
generate_pass_button.grid(row=3, column=2)

add_password_button = Button(text="Add", width=36, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

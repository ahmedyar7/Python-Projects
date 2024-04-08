from tkinter import *
from tkinter import messagebox


# * --------- CONSTANSTS ---------------- * #
my_email = "ahmedyar778@gmail.com"

# * ------------- GENERATE RANDOM PASSWORD --------------- * #


# * ----------------------- SAVE PASSWORD ----------------------


def save():
    """Take the enteries and the store it into a data file"""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error", message="None of the feilds could remain empty"
        )

    else:
        with open("Password Manager/data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {email} | {password} \n")

            messagebox.askokcancel(
                title="Confirm", message=" Are you sure of the following enteries"
            )
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

generate_pass_button = Button(text="Generate")
generate_pass_button.grid(row=3, column=2)

add_password_button = Button(text="Add", width=36, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

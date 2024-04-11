import smtplib
import random


FILE_PATH = "Monday Motivation/quotes.txt"

with open(file=FILE_PATH) as quotes_file:
    quotes = random.choice(quotes_file.readlines())


MY_EMAIL = "your_email@email.com"
PASSWORD = "YOUR APP PASSWORD"

SUBJECT = "Monday Motivation \n\n"
MESSAGE = quotes

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: {SUBJECT} {MESSAGE}"
    )

from os import getenv
from dotenv import find_dotenv, load_dotenv
from requests import get
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

## Environment Variables => Amazon.com
USER_AGENT = getenv("USER_AGENT")
ACCEPT_LANGUAGE = getenv("ACCEPT_LANGUAGE")
URL = getenv("URL")

## Environment Variables => SMTP
TO_EMAIL = getenv("TO_EMAIL")
FROM_EMAIL = getenv("FROM_EMAIL")
PASSWORD = getenv("PASSWORD")
SMTP_SEVER = getenv("SMTP_SEVER")

HEADER = {
    "User-Agent": USER_AGENT,
    "Accept_Language": ACCEPT_LANGUAGE,
}

response = get(url=URL, headers=HEADER)
data = response.text

soup = BeautifulSoup(markup=data, features="html.parser")

price = soup.find(name="span", class_="a-size-base a-color-secondary").text
formmated_price = price.lstrip().replace("$", "")


book_price = float(formmated_price)
desired_price = 10.00

# Creating the Email Object:-
message = EmailMessage()
message["Subject"] = "Amazon Price Tracker 🔍🔎"
message.set_content("The Price has Dropped 📉📉")
message["From"] = FROM_EMAIL
message["To"] = TO_EMAIL


if book_price <= desired_price:
    with smtplib.SMTP(host=SMTP_SEVER, port=587) as connection:
        connection.starttls()
        connection.login(TO_EMAIL, PASSWORD)
        connection.send_message(message)

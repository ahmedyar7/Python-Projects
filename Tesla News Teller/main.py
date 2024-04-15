import os
from dotenv import load_dotenv, find_dotenv
from requests import get
import smtplib
from html import unescape


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


# Getting hold of Environment Variable:
API_KEY = os.getenv("API_KEY")

SMTP_LIVE_SERVER = os.getenv("SMTP_LIVE_SERVER")
MY_EMAIL = os.getenv("MY_EMAIL")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
PASSOWRD = os.getenv("PASSOWRD")

API_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla"

parameters = {
    "apiKey": API_KEY,
    "q": COMPANY_NAME,
}

article = get(url=API_ENDPOINT, params=parameters)
article.raise_for_status

article_data = article.json().get("articles")

# TODO Import the smtplib and make smtp live server and send mail

i = 0
i += 1


source_name = article_data[i].get("source").get("name")
article_author = article_data[i].get("author")
article_title = article_data[i].get("title")
article_description = article_data[i].get("description")

MESSAGE = unescape(
    f"Source:{source_name}\nAuthor:{article_author}\nTitle:{article_title}\nDescription:{article_description}"
)

with smtplib.SMTP(SMTP_LIVE_SERVER) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, PASSOWRD)

    connection.sendmail(
        to_addrs=YOUR_EMAIL,
        from_addr=MY_EMAIL,
        msg=f"Subject:Tesla Alert\n\n{MESSAGE}",
    )

print("SUCCESS")

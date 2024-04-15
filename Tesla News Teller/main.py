import os
from dotenv import load_dotenv, find_dotenv
from requests import get
import smtplib
from html import unescape


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


# Getting hold of Environment Variable:
API_KEY = os.getenv("API_KEY")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

TWILIO_PHONENUMBER = os.getenv("TWILIO_PHONENUMBER")
MY_PHONENUMBER = os.getenv("MY_PHONENUMBER")

API_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla"

parameters = {
    "apiKey": API_KEY,
    "q": COMPANY_NAME,
}

article = get(url=API_ENDPOINT, params=parameters)
article.raise_for_status

article_data = article.json().get("articles")


daily = 0
daily += 1
source_name = article_data[daily].get("source").get("name")
article_author = article_data[daily].get("author")
article_title = article_data[daily].get("title")
article_description = article_data[daily].get("description")

MESSAGE = f"Source:{source_name}\nAuthor:{article_author}\nTitle:{article_title}\nDescription:{article_description}"

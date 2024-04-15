import os
from dotenv import load_dotenv, find_dotenv
from requests import get


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


# Getting hold of Environment Variable:
API_KEY = os.getenv("API_KEY")

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
first_three_articles = article_data[:3]

# TODO Import the smtplib and make smtp live server and send mail


for i in range(3):
    source_name = article_data[i].get("source").get("name")
    article_author = article_data[i].get("author")
    article_title = article_data[i].get("title")
    article_description = article_data[i].get("description")

    message = f"Source: {source_name} \n Author: {article_author} \n Title: {article_title} \n Description: {article_description}"

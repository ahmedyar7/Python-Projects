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
# first_three_articles = article_data[:3]

# TODO : Get the  articles[0].source{"id": null,"name": "Digital Trends"}
# TODO : Get the  articles[0].source and the author title and description

# TODO : But first get hold of only 1 article data

source_name = article_data[0].get("source").get("name")
article_author = article_data[0].get("author")
article_title = article_data[0].get("title")
article_description = article_data[0].get("description")

print(source_name)
print(article_author)
print(article_title)
print(article_description)

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

# TODO : Get hold of all articles of yesterday
# TODO: Get hold of only 2 articles from yesterday

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
print(len(first_three_articles))

from os import getenv
from dotenv import find_dotenv, load_dotenv
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Holding the Environment Variables
load_dotenv(dotenv_path=find_dotenv())
USER_AGENT = getenv("USER_AGENT")


class AmazonScraper:
    def __init__(self) -> None:

        # Sending the HTTPS Request
        self.headers = {
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US",
        }
        self.respones = requests.get(
            url="https://www.daraz.pk/catalog/?q=books&_keyori=ss&from=input&spm=a2a0e.8553159.search.go.7102332d0ot1sT",
            headers=self.headers,
        )
        print(self.respones.status_code)
        self.data = self.respones.text
        # print(self.data)

        # Scraping using the BeautifullSoup:
        self.soup = BeautifulSoup(markup=self.data, features="html.parser")

        # Getting hold of the anchor tag:
        self.anchor_tags = self.soup.find(name="div", attrs={"id": "id-title"})
        print(self.anchor_tags.string)


amazon = AmazonScraper()
# <div class="title-wrapper--IaQ0m" id="id-title">HOW TO ANALYZE PEOPLE WITH DARK PSYCHOLOGY Book by Liam Robinson KS</div>

from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Quotes:
    def __init__(self) -> None:
        """This function would fetch the relevent qoute from the api"""

        self.response = get(url="https://zenquotes.io/api/quotes/")
        self.quote_text = self.response.json()[0].get("q")
        self.quote_author = self.response.json()[0].get("a")

class TwitterBot:
    def __init__(self) -> None:
        pass
        # self.get_quote()


    def tweet_login(self):
        """This method would  use selenium to tweet the random quote that is generated"""

        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)

        self.driver.get(url="https://twitter.com/i/flow/login")




bot = TwitterBot()
bot.tweet()

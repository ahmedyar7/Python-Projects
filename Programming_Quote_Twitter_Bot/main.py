from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import getenv
from dotenv import find_dotenv, load_dotenv

load_dotenv(dotenv_path=find_dotenv())
USERNAME = getenv("USER_NAME")
PASSWORD = getenv("PASSWORD")
EMAIL = getenv("EMAIL")


class Quotes:
    def __init__(self) -> None:
        """This function would fetch the relevent qoute from the api"""

        self.response = get(url="https://zenquotes.io/api/quotes/")
        self.quote_text = self.response.json()[0].get("q")
        self.quote_author = self.response.json()[0].get("a")


class TwitterBot:
    def __init__(self, quotes: Quotes) -> None:

        # Compostion object of quotes class
        self.quote = quotes

        # Selenium Setup:
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = self.driver.implicitly_wait(30)

    def tweet_login(self) -> None:
        """This method would  use selenium to tweet the random quote that is generated"""

        self.driver.get(url="https://twitter.com/i/flow/login")

        self.wait
        self.email = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input",
        )
        self.email.send_keys(EMAIL)
        self.email.send_keys(Keys.ENTER)

        self.wait
        self.input_username = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
        )
        self.input_username.send_keys(USERNAME)
        self.input_username.send_keys(Keys.ENTER)

        self.wait
        self.input_password = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        )
        self.input_password.send_keys(PASSWORD)
        self.input_password.send_keys(Keys.ENTER)

    def tweet_quote(self) -> None:
        """This would tweet the quote"""

        self.tweet = f"{self.quote.quote_text}\n{self.quote.quote_author}"

        self.wait
        self.tweet_textbox = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div",
        )
        self.tweet_textbox.send_keys(self.tweet)

        self.wait
        self.post_button = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div",
        )
        self.post_button.click()


quotes = Quotes()

bot = TwitterBot(quotes)
bot.tweet_login()
bot.tweet_quote()

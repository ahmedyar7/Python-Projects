from os import getenv
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

load_dotenv(dotenv_path=find_dotenv())


## Environment Variables => Twitter
TWITTER_EMAIL = getenv("TWITTER_EMAIL")
TWITTER_USERNAME = getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = getenv("TWITTER_PASSWORD")


## Constants
INTERNET_SPEED = "20Mpbs"

ISP = "YOUR ISP"


class TwitterBot:

    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = self.driver.implicitly_wait(30)

        self.find_internet_speed()
        self.twitter_login()
        self.tweet()

    def find_internet_speed(self):

        self.wait = self.driver.implicitly_wait(30)
        self.driver.get("https://fast.com/")

        sleep(7)
        self.internet_speed = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/div[1]/div[2]/div/div[1]"
        ).text

    def twitter_login(self):
        """This would login to one's twitter account"""

        self.driver.get(url="https://twitter.com/i/flow/login")

        self.wait

        email_login = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input",
        )
        email_login.send_keys(TWITTER_EMAIL)
        email_login.send_keys(Keys.ENTER)

        self.wait

        try:
            username_login = self.driver.find_element(
                by=By.XPATH,
                value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
            )

            username_login.send_keys(TWITTER_USERNAME)
            username_login.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

        self.wait

        password_login = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        )
        password_login.send_keys(TWITTER_PASSWORD)
        password_login.send_keys(Keys.ENTER)

    def tweet(self):
        """This will write the tweet"""

        self.wait

        tweet_textbox = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div",
        )
        post_button = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div",
        )

        global INTERNET_SPEED, ISP

        tweet_msg = f"Dear {ISP}\n My Promised Internet Speed is {INTERNET_SPEED}, and I am getting {self.internet_speed}, Please do something about it"

        tweet_textbox.send_keys(tweet_msg)
        post_button.send_keys(Keys.ENTER)

        self.driver.quit()


bot = TwitterBot()

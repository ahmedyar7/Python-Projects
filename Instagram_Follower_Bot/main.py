from os import getenv
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_dotenv(dotenv_path=find_dotenv())

# Environment Variables => instagram.com
EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstagramFollowerBot:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.instagram_login()

    def instagram_login(self) -> None:
        """This will login to the instgram page"""

        self.driver.get(url="https://www.instagram.com/")
        sleep(7)

        email_input = self.driver.find_element(
            by=By.XPATH, value="//*[@id='loginForm']/div/div[1]/div/label/input"
        )
        email_input.send_keys(EMAIL)

        password_input = self.driver.find_element(
            by=By.XPATH, value="//*[@id='loginForm']/div/div[2]/div/label/input"
        )
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

        print("login success full")


bot = InstagramFollowerBot()

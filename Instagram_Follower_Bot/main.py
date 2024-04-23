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

ACCOUNT_USERNAME = "ahmedyar.7"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstagramFollowerBot:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.instagram_login()
        # self.get_follow()

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

        sleep(3)

        not_now_button = self.driver.find_element(
            by=By.CLASS_NAME,
            value="_a9--._ap36._a9_0",
        )
        not_now_button.click()

    def get_follow(self):
        """This will follow the instagram account"""

        sleep(3)
        self.driver.get(url=f"https://www.instagram.com/{ACCOUNT_USERNAME}")
        sleep(3)

        account_follow = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div/button",
        )
        account_follow.click()


bot = InstagramFollowerBot()

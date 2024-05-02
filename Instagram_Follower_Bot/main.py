from os import getenv
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv(dotenv_path=find_dotenv())

# Environment Variables => instagram.com
EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASSWORD")

ACCOUNT_USERNAME = "zohakh67"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstagramFollowerBot:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = self.driver.implicitly_wait(30)
        self.instagram_login()
        self.get_follow()

    def instagram_login(self) -> None:
        """This will login to the instgram page"""

        self.driver.get(url="https://www.instagram.com/")
        self.wait

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

        self.wait

        # not_now_button = self.driver.find_element(
        #     by=By.CLASS_NAME,
        #     value="_a9--._ap36._a9_0",
        # )
        # not_now_button.click()

    def get_follow(self):
        """This will follow the instagram account"""

        self.wait
        self.driver.get(url=f"https://www.instagram.com/{ACCOUNT_USERNAME}")
        self.wait

        account_follow = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/div/div/button/div",
        )
        account_follow.click()


bot = InstagramFollowerBot()

from os import getenv
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


load_dotenv(dotenv_path=find_dotenv())


# Environment Variables => Twitter
TWITTER_EMAIL = getenv("TWITTER_EMAIL")
TWITTER_USERNAME = getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = getenv("TWITTER_PASSWORD")

# Setting up Selenium:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = driver.implicitly_wait(30)


class TwitterNetBot:

    def get_internet_speed():
        """This will get the internet speed"""

        driver.get(url="https://www.speedtest.net/")
        wait

        go_button = driver.find_element(
            by=By.XPATH,
            value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]",
        )
        go_button.click()
        print("GOT CLICKED")

        wait

        global upload_speed, download_speed

        upload_speed = driver.find_element(
            by=By.XPATH,
            value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span",
        ).text
        download_speed = driver.find_element(
            by=By.XPATH,
            value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span",
        ).text

        print(download_speed)
        print(upload_speed)


bot = TwitterNetBot
bot.get_internet_speed()
bot.twitter_login()
bot.tweet()

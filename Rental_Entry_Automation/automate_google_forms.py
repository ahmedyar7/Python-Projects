from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

GOOGLE_FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSd92K14BKZ3pWoT1sV3T5o7QqXK8e5-rRcjkJ8MLvzBhNF64g/viewform?usp=sf_link"


class AutomateGoogleForms:

    def __init__(self) -> None:

        # Chrome Setup:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        # Selenium Setup:
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url=GOOGLE_FORMS_LINK)

        # Address Input:
        sleep(7)
        self.address_input = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
        )
        self.price_input = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
        )
        self.address_link_input = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
        )
        self.submit_buttons = self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div",
        )
        self.address_input.send_keys("Ahmed Yar")

        # Price Input
        self.price_input.send_keys("Ahmed Yar")

        # Address Link Input:
        self.address_link_input.send_keys("Ahmed Yar")

        # Submit Button:
        self.submit_buttons.click()


forms = AutomateGoogleForms()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


timeout = time() + 10  # 5sec interval delay
stop_time = time() + (5 * 60)  # 5 mins


def click_and_buy():
    """This function would click and bye the most expensive item"""
    upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store>div:not(.grayed)")
    upgrades[-1].click()


cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")

while time() <= stop_time:
    cookie.click()
    if timeout <= time():
        click_and_buy()
        timeout = time() + 10
        timeout += 1

cookies_sec = driver.find_element(by=By.CSS_SELECTOR, value="#cps")
print(f"cookies/sec = {cookies_sec}")

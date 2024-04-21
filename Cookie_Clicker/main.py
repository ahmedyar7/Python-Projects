from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")

# TODO: Get hold of the store items in a list
store_items = []
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")

for item in items:
    element_text = item.text
    if element_text != "":
        cost = element_text.split("-")[1].strip().replace(",", "")
        store_items.append(cost)

print(store_items)


# while True:
#     cookie.click()

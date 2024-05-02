from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RecipeRecommendation:

    def __init__(self) -> None:

        # Selenium Setup:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = self.driver.implicitly_wait(30)

        self.driver.get(url="https://www.allrecipes.com/")
        self.wait

        # Input Ingredients:
        self.input_ingredients = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/header/div[1]/div[3]/ul/li[1]/div/form/div/input",
        )
        self.input_ingredients.send_keys("rice and chicken")
        self.ingredient_button = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/header/div[1]/div[3]/ul/li[1]/div/form/div/button",
        )
        self.ingredient_button.click()


recipie = RecipeRecommendation()
# /html/body/header/div[1]/div[3]/ul/li[1]/div/form/div/button

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class RecipeRecommendation:

    def __init__(self) -> None:

        # Selenium Setup:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = self.driver.implicitly_wait(30)

        self.driver.get(url="https://www.foodnetwork.com/")
        self.wait

        # Add Handling:
        try:
            self.ads = self.driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/div/div/form/div[1]/a[2]"
            )
            self.ads.click()
        except NoSuchElementException:
            pass

        self.wait
        # Input Ingredients:
        self.input_ingredients = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/section/div[1]/header/section[2]/div/div[10]/section/form/div/span/input",
        )
        self.input_ingredients.send_keys("rice and chicken")
        self.input_ingredients.send_keys(Keys.ENTER)

        self.recipies_url = self.driver.current_url
        print(self.recipies_url)

    def get_recipies(self):
        self.recipies = []
        self.all_recipies = self.driver.find_elements(
            by=By.CSS_SELECTOR, value="div .m-MediaBlock__a-HeadlineText"
        )
        for recps in self.recipies:
            self.recipies.append(recps.text)
        print(self.recipies)


recipie_recommendation = RecipeRecommendation()
recipie_recommendation.get_recipies()

from requests import get
from bs4 import BeautifulSoup


class Recipes:
    def __init__(self) -> None:
        self.response = get("https://www.foodnetwork.com/search/rice-and-chicken-")
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "html.parser")

    def get_all_recipes(self):
        """This function would get all the recipes for the given ingredients:"""

        # TODO : Then find all the receipes for the given ingredieents

        self.find_recipies = self.soup.find_all(
            name="span", class_="m-MediaBlock__a-HeadlineText"
        )
        self.all_recipies = []

        for recipies in self.find_recipies:
            recipies_txt = recipies.text
            self.all_recipies.append(recipies_txt.replace(" \n ", "").strip())

        print(self.all_recipies[2])


if __name__ == "__main__":
    recipies = Recipes()
    recipies.get_all_recipes()
# <div class="m-MediaBlock__a-HeadlineText" data-truncate="50">Jeweled Rice and Chicken Soup </div>

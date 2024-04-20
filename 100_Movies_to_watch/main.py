from bs4 import BeautifulSoup
import requests


response = requests.get(
    url="https://www.empireonline.com/movies/features/best-movies-2/"
)
data = response.text

soup = BeautifulSoup(markup=data, features="html.parser")
# <h3 class="listicleItem_listicle-item__title__BfenH">99) Groundhog Day</h3>
first_movie = soup.find(name="h3", class_="listicleItem_listicle-item__title__BfenH")

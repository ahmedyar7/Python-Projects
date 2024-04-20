from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
MARKUP_PARSER = "html.parser"


response = requests.get(
    url="",
)
data = response.text

soup = BeautifulSoup(
    markup=data,
    features=MARKUP_PARSER,
)
movies = soup.find_all(
    name="h3",
    class_="listicleItem_listicle-item__title__BfenH",
)

all_movies = []
for movie in movies:
    all_movies.append(movie.get_text())

all_films = all_movies[::-1]  # Reversing the list of movies to start from 1

with open(file="100_movies_to_watch.txt", mode="a") as file:
    for movie in all_films:
        file.write(f"{movie}\n")

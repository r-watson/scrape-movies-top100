import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_text = result.text
# print(movies_text)

soup = BeautifulSoup(movies_text, "html.parser")
# print(soup.prettify())

movies = soup.select(".listicle-item picture img")
# print(type(movies))

number = 1
all_movies = [movie.get("alt") for movie in movies[::-1]]
with open("data/movie_list.txt", mode="w") as file:
    for movie in all_movies:
        file.write(f"{number}) {movie}\n")
        number += 1

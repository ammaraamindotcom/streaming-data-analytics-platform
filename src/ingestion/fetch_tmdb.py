import os
import requests
import pandas as pd
from dotenv import load_dotenv

print("🔥 FILE EXECUTED 🔥")


load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies(page=1):
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["results"]

def main():
    all_movies = []
    for page in range(1, 6):  
        movies = fetch_movies(page)
        all_movies.extend(movies)

    df = pd.DataFrame(all_movies)
    df = df[["id", "title", "release_date", "vote_average", "genre_ids"]]

    os.makedirs("data/raw/tmdb", exist_ok=True)
    df.to_csv("data/raw/tmdb/popular_movies.csv", index=False)
    print("Saved TMDB data!")

if __name__ == "__main__":
    main()

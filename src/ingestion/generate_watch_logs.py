import os
import random
import pandas as pd
from datetime import datetime, timedelta

# Config
NUM_USERS = 500
NUM_EVENTS = 5000

DEVICES = ["mobile", "tv", "laptop", "tablet"]
REGIONS = ["US", "EU", "ASIA", "LATAM"]

RAW_DATA_PATH = "data/raw/logs"
TMDB_DATA_PATH = "data/raw/tmdb/popular_movies.csv"

def generate_watch_logs():
    movies = pd.read_csv(TMDB_DATA_PATH)
    movie_ids = movies["id"].tolist()

    events = []

    for _ in range(NUM_EVENTS):
        event = {
            "user_id": random.randint(1, NUM_USERS),
            "title_id": random.choice(movie_ids),
            "watch_duration_minutes": random.randint(5, 180),
            "device": random.choice(DEVICES),
            "region": random.choice(REGIONS),
            "event_timestamp": (
                datetime.now() - timedelta(minutes=random.randint(0, 60 * 24 * 30))
            ).isoformat()
        }
        events.append(event)

    df = pd.DataFrame(events)
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    df.to_csv(f"{RAW_DATA_PATH}/watch_events.csv", index=False)

    print("Generated simulated watch logs!")

if __name__ == "__main__":
    generate_watch_logs()
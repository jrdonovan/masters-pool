from datetime import datetime, timedelta
import json
import os

CACHE_DIR = "data/cache"
CACHE_TTL_MINS = 5  # Cache Time-To-Live in minutes


def get_cache_filename(timestamp: datetime, subfolder) -> str:
    return os.path.join(
        f"{CACHE_DIR}/{subfolder}",
        f"{subfolder}_{timestamp.strftime('%Y%m%d_%H%M%S')}.json",
    )


def get_latest_cache_file(subfolder: str) -> str:
    if not os.path.exists(CACHE_DIR):
        print(f"Cache directory {CACHE_DIR} does not exist.")
        return None
    cache_path = f"{CACHE_DIR}/{subfolder}"
    if not os.path.exists(cache_path):
        print(f"Cache subdirectory {cache_path} does not exist.")
        return None
    files = [f for f in os.listdir(cache_path) if f.endswith(".json")]
    if not files:
        print("No cache files found.")
        return None
    files = sorted(files, reverse=True)
    latest_cache_file = os.path.join(cache_path, files[0])
    print(f"Latest cache file: {latest_cache_file}")
    return latest_cache_file


def is_cache_fresh(filepath: str) -> bool:
    if not filepath or not os.path.exists(filepath):
        print("Cache file does not exist.")
        return False
    modified_time = datetime.fromtimestamp(os.path.getmtime(filepath))

    since_last_refresh = datetime.now() - modified_time
    is_fresh = since_last_refresh < timedelta(minutes=CACHE_TTL_MINS)
    if is_fresh:
        print(f"Cache file {filepath} is fresh.")
    else:
        print(f"Cache file {filepath} is stale.")
    return is_fresh


def load_from_cache(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def save_to_cache(data: dict, subfolder: str) -> None:
    cache_path = f"{CACHE_DIR}/{subfolder}"
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
    filepath = get_cache_filename(datetime.now(), subfolder)
    with open(filepath, "w") as f:
        json.dump(data, f)

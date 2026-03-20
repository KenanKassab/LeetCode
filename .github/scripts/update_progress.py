import re
import requests
import pathlib
import sys
import time

USERNAME = "knkn97"
README = pathlib.Path("README.md")
MAX_RETRIES = 3
TIMEOUT = 30  # seconds

def fetch_stats():
    url = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Attempt {attempt}: Fetching {url}")
            r = requests.get(url, timeout=TIMEOUT)
            r.raise_for_status()
            stats = r.json()
            # Basic validation
            if all(key in stats for key in ["easySolved", "mediumSolved", "hardSolved"]):
                return stats
            else:
                print("Response missing expected keys:", stats.keys())
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
        except ValueError as e:
            print(f"Attempt {attempt} failed (JSON decode): {e}")
            print("Response text:", r.text[:200])
        
        if attempt < MAX_RETRIES:
            wait = 2 ** attempt  # 2, 4, ... seconds
            print(f"Retrying in {wait} seconds...")
            time.sleep(wait)
    
    print("All attempts failed. Exiting.")
    sys.exit(1)

def update_readme():
    stats = fetch_stats()
    easy = stats["easySolved"] or 0
    medium = stats["mediumSolved"] or 0
    hard = stats["hardSolved"] or 0
    
    print(f"Fetched: Easy={easy}, Medium={medium}, Hard={hard}")
    
    text = README.read_text()
    text = re.sub(r"(\| 🟢 Easy\s*\|\s*)\d+", lambda m: f"{m.group(1)}{easy}", text)
    text = re.sub(r"(\| 🟡 Medium\s*\|\s*)\d+", lambda m: f"{m.group(1)}{medium}", text)
    text = re.sub(r"(\| 🔴 Hard\s*\|\s*)\d+", lambda m: f"{m.group(1)}{hard}", text)
    README.write_text(text)
    print("✅ README updated successfully!")

if __name__ == "__main__":
    update_readme()

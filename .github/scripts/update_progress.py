import re
import requests
import pathlib
import sys
import time

USERNAME = "knkn97"
README = pathlib.Path("README.md")

def fetch_stats():
    # Alternative API endpoint
    url = f"https://alfa-leetcode-api.onrender.com/{USERNAME}/solved"
    for attempt in range(1, 4):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            data = r.json()
            # The response contains 'easySolved', 'mediumSolved', 'hardSolved'
            return data
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < 3:
                time.sleep(2 ** attempt)
    print("All attempts failed.")
    sys.exit(1)

def update_readme():
    stats = fetch_stats()
    easy = stats.get("easySolved", 0)
    medium = stats.get("mediumSolved", 0)
    hard = stats.get("hardSolved", 0)

    print(f"Fetched: Easy={easy}, Medium={medium}, Hard={hard}")

    text = README.read_text()
    text = re.sub(r"(\| 🟢 Easy\s*\|\s*)\d+", lambda m: f"{m.group(1)}{easy}", text)
    text = re.sub(r"(\| 🟡 Medium\s*\|\s*)\d+", lambda m: f"{m.group(1)}{medium}", text)
    text = re.sub(r"(\| 🔴 Hard\s*\|\s*)\d+", lambda m: f"{m.group(1)}{hard}", text)
    README.write_text(text)
    print("✅ README updated successfully!")

if __name__ == "__main__":
    update_readme()

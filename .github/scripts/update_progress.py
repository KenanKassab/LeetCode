import re
import requests
import pathlib
import sys

USERNAME = "knkn97"
README = pathlib.Path("README.md")

def update_readme():
    url = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()                     # Raise exception for 4xx/5xx
        stats = r.json()                         # May raise JSONDecodeError
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        sys.exit(1)
    except ValueError as e:                      # JSONDecodeError is a ValueError subclass
        print(f"❌ Invalid JSON response: {e}")
        print(f"Response text: {r.text[:200]}")  # Show first 200 chars for debugging
        sys.exit(1)

    # Ensure the expected keys exist
    required_keys = ["easySolved", "mediumSolved", "hardSolved"]
    if not all(key in stats for key in required_keys):
        print("❌ Missing expected keys in JSON response")
        print("Received keys:", stats.keys())
        sys.exit(1)

    easy = stats["easySolved"]
    medium = stats["mediumSolved"]
    hard = stats["hardSolved"]

    # Optional: fallback if values are None
    easy = easy or 0
    medium = medium or 0
    hard = hard or 0

    total_easy, total_medium, total_hard = 650, 1400, 350  # Total problem counts (you may want to update these)

    print(f"Fetched: Easy={easy}, Medium={medium}, Hard={hard}")

    text = README.read_text()

    # Use lambda to replace numbers safely
    text = re.sub(r"(\| 🟢 Easy\s*\|\s*)\d+", lambda m: f"{m.group(1)}{easy}", text)
    text = re.sub(r"(\| 🟡 Medium\s*\|\s*)\d+", lambda m: f"{m.group(1)}{medium}", text)
    text = re.sub(r"(\| 🔴 Hard\s*\|\s*)\d+", lambda m: f"{m.group(1)}{hard}", text)

    README.write_text(text)
    print("✅ README updated successfully!")

if __name__ == "__main__":
    update_readme()

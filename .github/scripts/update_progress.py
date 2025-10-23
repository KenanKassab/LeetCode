import re, requests, pathlib

USERNAME = "knkn97"
README = pathlib.Path("README.md")

def update_readme():
    # Fetch stats
    url = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"
    r = requests.get(url)
    stats = r.json()

    easy, medium, hard = stats["easySolved"], stats["mediumSolved"], stats["hardSolved"]
    total_easy, total_medium, total_hard = 650, 1400, 350  # Total problems (static)

    print(f"Fetched: Easy={easy}, Medium={medium}, Hard={hard}")

    text = README.read_text()

    # Replace solved numbers
    text = re.sub(r"(\| 🟢 Easy\s*\|\s*)\d+", rf"\1{easy}", text)
    text = re.sub(r"(\| 🟡 Medium\s*\|\s*)\d+", rf"\1{medium}", text)
    text = re.sub(r"(\| 🔴 Hard\s*\|\s*)\d+", rf"\1{hard}", text)

    README.write_text(text)
    print("✅ README updated successfully")

if __name__ == "__main__":
    update_readme()

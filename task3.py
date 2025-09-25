import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML from CNN
url = "https://edition.cnn.com"   # CNN international homepage
response = requests.get(url)
response.raise_for_status()

# Step 2: Parse <h2> or <title> tags
soup = BeautifulSoup(response.text, "html.parser")
titles = []

# Extract <h2> tags
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text:
        titles.append(text)

# Extract <title> tag
page_title = soup.title.string if soup.title else None
if page_title:
    titles.insert(0, page_title.strip())

# Step 3: Save to .txt file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, title in enumerate(titles, start=1):
        f.write(f"{i}. {title}\n")

print(f"✅ Saved {len(titles)} titles from CNN to 'headlines.txt'")

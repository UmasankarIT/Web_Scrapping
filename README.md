📰 News Headlines Scraper
📌 Overview

This project is a simple Python web scraper that fetches the latest news headlines from a selected news website (e.g., CNN, BBC). It uses Requests to fetch HTML and BeautifulSoup to parse <h2> and <title> tags. The scraped headlines are saved in a headlines.txt file.

⚙️ Tools Used

Python 3

Requests

BeautifulSoup (bs4)

🚀 How to Run

Clone the repository

git clone https://github.com/your-username/news-headlines-scraper.git
cd news-headlines-scraper


Install dependencies

pip install requests beautifulsoup4

Run the script

python headline_scraper.py


Check the results
Headlines will be saved in:

headlines.txt

📂 Output Example (headlines.txt)
1. CNN - Breaking News, Latest News and Videos
2. Top stories right now
3. US election 2024 updates
4. Global economy outlook
5. Sports highlights

✨ Features

Scrapes <h2> and <title> tags

Saves results in a .txt file

Easy to switch between news sites (CNN, BBC, etc.)

print("S128 Aafiya Shaikh")

import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

print("First 3 Paragraphs:")
for p in paragraphs[:3]:
    print(p.get_text(strip=True))
    print()

images = soup.find_all("img")

print("Image Source URLs:")
for img in images:
    print(img.get("src"))

links = soup.find_all("a")

print("\nTotal number of links:", len(links))

headings = soup.find_all(["h1", "h2", "h3"])

print("\nHeadings:")
for heading in headings:
    print(heading.get_text(strip=True))

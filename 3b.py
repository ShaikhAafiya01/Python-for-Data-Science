from bs4 import BeautifulSoup

with open("example.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

text = soup.get_text()

print("Extracted data:")
print(text)

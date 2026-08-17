from bs4 import BeautifulSoup

with open("example2.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

text = soup.get_text()

print("Extracted Text:")
print(text)

word = input("\nEnter the word to search: ")

if word.lower() in text.lower():
    print("Word found!")
else:
    print("Word not found!")

with open("sample.txt", "r") as file:
    text = file.read()

print("File Content:")
print(text)

word = input("\nEnter the word to search: ")

if word.lower() in text.lower():
    print("Word found!")
else:
    print("Word not found!")

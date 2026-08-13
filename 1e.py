def process_sentence():
    sentence = input("Enter a sentence: ")

    word_count = len(sentence.split())
    char_count = len(sentence)

    lower_case = sentence.lower()
    upper_case = sentence.upper()

    replaced_sentence = sentence.replace(" ", "_")

    print("\n=== Sentence Analysis ===")
    print("Original Sentence :", sentence)
    print("Word Count        :", word_count)
    print("Character Count   :", char_count)
    print("Lowercase         :", lower_case)
    print("Uppercase         :", upper_case)
    print("With Underscores  :", replaced_sentence)
    print("=========================")

process_sentence()

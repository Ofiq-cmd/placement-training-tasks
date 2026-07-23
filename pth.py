def display_frequency(word, count):
    print(f"{word} : {count}")

dictionary = {}
try:
    with open("words.txt", "r") as file:
        for raw_word in file:
            word = raw_word.strip()
            if word:
                count = len(word)
                display_frequency(word, count)
                dictionary[word] = count
except FileNotFoundError:
    print("File not found.")
for word, count in dictionary.items():
    print(f"{word} : {count}")
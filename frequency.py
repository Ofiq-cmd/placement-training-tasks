word = input("Enter a word: ")
frequency = {}
for letter in word:
    if letter in word:
        frequency[letter] = frequency.get(letter, 0) + 1
print("Frequency :", frequency)
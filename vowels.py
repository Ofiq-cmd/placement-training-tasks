name = input("Enter your name: ")
vowels = 'aeiouAEIOU'
count = 0
for char in name:
    if char in vowels:
        count += 1
print("vowels count: ", count)
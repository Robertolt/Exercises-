word = input('Input a word:' )
vowels = ['a','e','i','o','u']
found = []



for letters in word:
    if letters in vowels:
        if letters not in found:
            found.append(letters)
for letters in found:
    print(letters)


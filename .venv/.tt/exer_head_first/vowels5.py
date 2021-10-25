vowels = ['a','e','i','o','u']
word = input('Input a word:' )
found = {}
for letters in word:
    if letters in vowels:
        found.setdefault(letters, 0)
        found[letters] += 1

for v,k in sorted(found.items()):
    print(v, 'was found', k, 'time(s)')



word = input('Input a word:' )
vowels = set('aeiou')
d = sorted(vowels.intersection(set(word)))
print(d)
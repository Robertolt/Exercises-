word = input('Input a word:' )
found = {'a':0 ,
         'e':0 ,
         'i':0 ,
         'o':0 ,
         'u':0}

for letters in word:
    if letters in found:
        found[letters] = found[letters] =+ 1

for v,k in sorted(found.items()):
    print(v, 'was found', k, 'time(s)')



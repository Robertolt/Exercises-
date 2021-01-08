
word = 'bootles'

for b in range(99,0,-1):
    print( b, word, 'of beer on the wall')
    print( b, word, 'of beer')
    print('take one down')
    print('pass it around')

    if b == 1:
        print('no more beers on the wall')

    else:
        n_b = b - 1
        if n_b == 1:
            word = 'bootle'

        print(n_b, word, 'of beer on the wall')

    print()
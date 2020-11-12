def caracters_counter(f):
    result = {}
    for caracter in f:
        result[caracter] = result.get(caracter,0) + 1
    return result

if __name__ == '__main__':
    print(caracters_counter('robertolt'))
    print()
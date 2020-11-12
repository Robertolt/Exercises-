def contar_caracteres(s):

    caracteres_ordenados = sorted(s)
    print(caracteres_ordenados)
    """Here the sorted will put the letters like these: 
    for name, aenm"""
    caracter_anterior = caracteres_ordenados[0]
    """caracter here will be 'a'"""
    contagem = 1
    """And then, we start counting"""

    for caracter in caracteres_ordenados[1:]:
        """for letters in enm"""
        if caracter == caracter_anterior:
            """For letters equals to the last one, the function add one to the counter"""
            contagem += 1
        else:
            print(f'{caracter_anterior}{contagem}')
            caracter_anterior = caracter
            contagem = 1


if __name__ == '__main__':
    contar_caracteres('roberto')
    print()
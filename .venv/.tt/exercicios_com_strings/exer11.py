"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras
lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!

"""

palavra_escondida = input('Digite a palavra da forca: ').upper()

print('Jogo da forca! Descubra a palavra!')

print('A palavra é: ', end='')
for letra in palavra_escondida:
    print(f'_ ', end='')

conjunto_palavra = set(palavra_escondida)
conjunto_letras_digitadas = set()
print()
print()
erros = 0

while not conjunto_palavra.issubset(conjunto_letras_digitadas) and erros < 6:
    letra_digitada = input('Digite uma letra: ').upper()

    if letra_digitada in conjunto_letras_digitadas:
        print('Essa letra você já usou, tente outra.')
    else:
        conjunto_letras_digitadas.add(letra_digitada)
        if letra_digitada in conjunto_palavra:
            print('A palavra é: ', end='')
            for letra in palavra_escondida:
                if letra in conjunto_letras_digitadas:
                    print(f'{letra} ', end='')
                else:
                    print(f'_ ', end='')
        else:
            erros += 1
            print(f'Voce errou pela {erros}° vez')

        print('Letras já digitadas: ', conjunto_letras_digitadas)

if erros < 6:
    print('Parabéns, você venceu!')
else:
    print('Infelizmente, você perdeu!')

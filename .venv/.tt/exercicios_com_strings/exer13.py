"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma
palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo
texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""
from random import randint

palavra = 'paradoxal'
lista_palavra = list(palavra)
print(lista_palavra)

print('A palavra embaralhada é: ', end='')
for letras in range(len(lista_palavra)):
    letra_aleatoria = str(lista_palavra[randint(0, len(lista_palavra) - 1)])
    print(letra_aleatoria, end='')
    lista_palavra.remove(letra_aleatoria)

print()

for i in range(1, 7):
    chute = input('Digite a palavra organizada: ')
    if chute == palavra:
        print('Parabéns, você acertou!!!')
    else:
        print(f'Você errou pela {i}º vez de 6 tentativas')

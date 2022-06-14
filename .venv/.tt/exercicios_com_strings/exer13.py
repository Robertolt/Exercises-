"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma
palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo
texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""
from random import randint

palavra = list('lolozin')
print(palavra)

for letras in range(len(palavra)):
    letra_aleatoria = str(palavra[randint(0, len(palavra) - 1)])
    print(letra_aleatoria, end='')
    palavra.remove(letra_aleatoria)


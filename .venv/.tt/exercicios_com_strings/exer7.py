"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""

palavra = input('Contador de espaços e vogais! Digite a palavra desejada: ').lower()
vogais = ('a', 'e', 'i', 'o', 'u')
contagem_vogais = 0
contagem_espaços = 0

for letras in palavra:
    if letras in vogais:
        contagem_vogais += 1
    else:
        if letras == ' ':
            contagem_espaços += 1


print(contagem_espaços)
print(contagem_vogais)

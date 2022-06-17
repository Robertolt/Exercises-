"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do
aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

numero = ()
altura = ()

for _ in range(2):
    numero = tuple(input('Digite o número do aluno: '))
    altura = tuple(input('Digite a altura do aluno: '))

conjunto_final = zip(numero, altura)
print(conjunto_final)
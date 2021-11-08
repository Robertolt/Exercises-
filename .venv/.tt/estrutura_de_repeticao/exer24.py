"""Faça um programa que calcule o mostre a média aritmética de N notas."""

qntd_notas = int(input('informe a quantidade de notas: '))
soma = 0

for n in range(1, qntd_notas + 1):
    soma += float(input('Insira as notas: '))
    media = soma / n
    print(f'a média aritmética das notas é {media}')

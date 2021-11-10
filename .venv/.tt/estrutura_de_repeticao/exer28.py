"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o
valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

qntd_cds = int(input('Digite a quantidade de cds: '))
soma = 0

for n in range(1, qntd_cds + 1):
    soma = soma + float(input('Informe o valor de cada cd: '))
    media = soma/n
    print(f'o valor total investido é {soma}, e a média por cd é {media}')

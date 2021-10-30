"""Faça um programa que leia 5 números e informe o maior número."""

maximo = float(input('input a number: '))

for _ in range (4):
    maximo = max(maximo,float(input('input a number: ')))
    print(f'the max number until now is {maximo}')

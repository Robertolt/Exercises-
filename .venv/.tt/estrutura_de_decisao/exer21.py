"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão)."""

n1 = int(input('input an int number: '))

if n1 % 2 != 0:
    print('this number is an odd number')
else:
    print('this number is a pair number')
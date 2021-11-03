"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números impares."""

lista_de_pares = 0
lista_de_impares = 0

for _ in range(10):
    n = int(input('input a number: '))
    if n%2 == 0:
        lista_de_pares += 1
    else:
        lista_de_impares += 1

print(f'os numeros de pares e impares sao respectivamente {lista_de_pares}, {lista_de_impares}')





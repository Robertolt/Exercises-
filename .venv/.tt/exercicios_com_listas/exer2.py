"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = []

for _ in range(1, 11):
    numero = float(input(f'Digite {_}° número: '))
    lista.append(numero)

lista.reverse()
print(lista)

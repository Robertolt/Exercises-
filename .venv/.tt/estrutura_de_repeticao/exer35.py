"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário."""

numero_n = int(input('coloque até que número deseja-se procurar por primos: '))
primos = 2

divisores = 0
lista_primos = []

while primos <= numero_n:

    for contador in range(1, numero_n + 1):
        if primos % contador == 0:
            divisores += 1
    if divisores == 2:
        lista_primos.append(primos)
        divisores = 0
    else:
        divisores = 0

    primos += 1

print(f'a lista de primos é{lista_primos}')

"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""

numero_n = int(input('coloque até que número deseja-se procurar por primos: '))
primos = 2
numero_divisoes = 0
divisores = 0
lista_primos = []

while primos <= numero_n:

    for contador in range(1, numero_n + 1):
        if primos % contador == 0:
            divisores += 1
            numero_divisoes += 1
        else:
            numero_divisoes += 1
    if divisores == 2:
        lista_primos.append(primos)
        divisores = 0
    else:
        divisores = 0

    primos += 1

print(f'a lista de primos é{lista_primos}, e foram feitas {numero_divisoes} divisoes')

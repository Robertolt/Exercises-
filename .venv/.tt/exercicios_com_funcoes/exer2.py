"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def impressora_de_valores(n: int):
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(k, end='   ')
        print('\n')


impressora_de_valores(6)

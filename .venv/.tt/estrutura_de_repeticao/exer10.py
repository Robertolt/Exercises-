"""Faça um programa que receba dois números inteiros e gere os números inteiros que
estão no intervalo compreendido por eles."""

n1 = int(input('input the 1st integer number: '))
n2 = int(input('input the 2nd integer number: '))

if n1 < n2:
    n1 = n1 + 1
    for i in range(n1, n2):
        print(list(range(i)))
else:
    pass
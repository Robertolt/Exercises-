"""Faça um programa que receba dois números inteiros e gere os números inteiros que
estão no intervalo compreendido por eles."""

n1 = int(input('input the 1st integer number: '))  #ex:1
n2 = int(input('input the 2nd integer number: '))  #ex:10


print(list(range(n1+1, n2)))

#printar 2,3,4,5,6,7,8,9
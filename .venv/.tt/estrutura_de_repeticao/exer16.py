"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500"""

n = int(input('input the series n number >500: '))
ultimo = 1
penultimo = 1

if n == 1 or n == 2:
    print('n=1')
else:
    for _ in range(2, n):
        proximo = ultimo + penultimo
        penultimo = ultimo
        ultimo = proximo
    print(proximo)
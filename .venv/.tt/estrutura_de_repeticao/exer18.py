"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

lista = []
N_numeros = int(input('coloque a quantidade de números desejada: '))

for _ in range(N_numeros): # 0 1 2 3 4
    lista.append(int(input('digite os números desejados: ')))

print('o número máximo é', max(lista), 'o menor número é', min(lista), 'a soma é', sum(lista))

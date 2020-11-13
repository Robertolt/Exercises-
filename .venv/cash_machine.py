"""Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.

O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1."""

cash = int(input('How many dollars will you take, 10$<x<600$: '))

dolar100 = cash//100
cash -= dolar100*100

dolar50 = cash//50
cash -= dolar50*50

dolar10 = cash//10
cash -= dolar10*10

dolar5 = cash//5
cash -= dolar5*5

print('you got:')
print(dolar100,'hundred $ bills')
print(dolar50,'fifty $ bills')
print(dolar10,'ten $ bills')
print(dolar5,' five $ bills')
print(cash,'one $ bills')

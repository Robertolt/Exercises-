"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

fatorial = int(input('Insira o fatorial a ser calculado: '))
x = 1
valor = 1
lista = []
contador = fatorial

for _ in range(fatorial):
    valor *= x
    lista.append(x)
    x += 1

print(f'{fatorial}! = ')
for _ in range(contador - 1): # 0 1 2 3 4
    print(f'{contador}', end='.')
    contador -= 1
print(f'1 = {valor}')



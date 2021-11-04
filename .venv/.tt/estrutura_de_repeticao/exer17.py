"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""

fatorial = int(input('input a number: '))#5*4*3*2*1
primeiro = 1
numero = 1

for _ in range(fatorial):
    numero *= primeiro
    primeiro += 1

print(numero)

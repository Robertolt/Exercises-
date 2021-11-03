"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem."""

st_number = int(input('input the 1st number: '))
nd_number = int(input('input the 2nd number: '))
result = 1

for _ in range(nd_number): #0,1,2
    result *= st_number
    print(result)

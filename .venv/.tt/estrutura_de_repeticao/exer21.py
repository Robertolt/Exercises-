"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""

verificador_primo = int(input('coloque o número para vereficarmos se ele é primo: ')) #4
divisores = 0

for contador in range(1, verificador_primo + 1):  # 1 2 3 4
    if verificador_primo % contador == 0:
        divisores += 1

if divisores == 2:
    print(f'o {verificador_primo} é um número primo')
else:
    print(f'o {verificador_primo} não é um número primo')

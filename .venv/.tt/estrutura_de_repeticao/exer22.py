"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível."""

verificador_primo = int(input('coloque o número para vereficarmos se ele é primo: ')) #4
divisores = 0
lista_de_divisores = []

for contador in range(1, verificador_primo + 1):  # 1 2 3 4
    if verificador_primo % contador == 0:
        divisores += 1
        lista_de_divisores.append(contador)

if divisores == 2:
    print(f'o {verificador_primo} é um número primo')
else:
    print(f'o {verificador_primo} não é um número primo, e os divisores são {lista_de_divisores}')

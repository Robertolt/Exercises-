"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é
 ou não um número primo."""

inteiro = int(input('Digite o número para que o programa verifique se é um primo: ')) #7
divisor = 0

for x in range(1, inteiro + 1): # 0 1 2 3 4 5 6
    if inteiro % x == 0:
        divisor += 1

if divisor == 2:
    print('o inteiro inserido é um número primo')
else:
    print('o inteiro inserido não é um número primo')

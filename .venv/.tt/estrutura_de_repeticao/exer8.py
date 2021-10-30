"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

sum = float(input('input a number: '))

for n in range(2, 6):
    sum += float(input('input a number: '))
    rate = sum / n
    print(f'the sum is {sum}', f'and the rate in {rate}')



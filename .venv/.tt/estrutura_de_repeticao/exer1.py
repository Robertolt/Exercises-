"""Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""


while True:
    try:
        number = int(input('input a number: '))
    except ValueError:
        print('A integer number must be inputed')
    else:
        if 0 <= number <= 10:
            print(f'the number was {number}')
            break
        else:
            print('you must inform a number between 0 and 10')


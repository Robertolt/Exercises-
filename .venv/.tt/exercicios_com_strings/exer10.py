"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99
e imprima-o na tela por extenso.
"""

numero = int(input('Digite um número até 99: '))

dezena = numero // 10
unidade = numero % 10
if dezena == 1:
    dct_dezena_1 = {11: 'Onze', 12: 'Doze', 13: 'Treze', 14: 'Quatorze', 15: 'Quize', 16: 'Dezesseis', 17: 'Dezessete',
                    18: 'Dezoito', 19: 'Dezenove'}
    print(f'O seu número é o {dct_dezena_1[numero]}')
else:
    dct_dezena = {2: 'Vinte', 3: 'Trinta', 4: 'Quarente', 5: 'Cinquenta', 6: 'Sessenta', 7: 'Setenta', 8: 'Oitenta',
                  9: 'Noventa'}
    dct_unidade = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete',
                   8: 'oito', 9: 'nove'}
    print(f'O seu número é {dct_dezena[dezena]} e {dct_unidade[unidade]}')

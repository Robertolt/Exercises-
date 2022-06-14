"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no
caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

num_telefone = input('Digite o número de telefone: ')

if num_telefone.isdigit():
    if len(num_telefone) == 8:
        print(f'Telefone está correto, sem formatação é: {num_telefone}')
        print(f'Telefone está correto, com formatação é: {num_telefone[0:4] + "-" + num_telefone[4:]}')
    else:
        print(f'Telefone está faltando o 3, vou adicioná-lo, sem formatação é: {"3" + num_telefone}')
        print('Telefone está faltando o 3, vou adicioná-lo, com formatação é: '
              f'{"3" + num_telefone[0:3] + "-" + num_telefone[3:]}')
else:
    if len(num_telefone) == 9:
        print(f'Telefone está correto, sem formatação é: {num_telefone.replace("-", "")}')
        print(f'Telefone está correto, com formatação é: {num_telefone}')
    else:
        print(f'Telefone está faltando o 3, vou adicioná-lo, sem formatação é: {"3" + num_telefone.replace("-", "")}')
        print(f'Telefone está faltando o 3, vou adicioná-lo, com formatação é: {"3" + num_telefone}')


"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def funcao_soma_3(a1, a2, a3):
    resultado = a1 + a2 + a3
    return resultado


a1 = int(input('Digite o primeiro número: '))
a2 = int(input('Digite o segundo número: '))
a3 = int(input('Digite o terceiro número: '))

print('Soma: ', funcao_soma_3(a1, a2, a3))

"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
 se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def valor_variavel(n: int):
    if n > 0:
        return 'P'
    else:
        return 'N'


n = int(input('Digite o número desejado: '))
print('O número é: ', valor_variavel(n))

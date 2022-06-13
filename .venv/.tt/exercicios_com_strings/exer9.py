"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
 e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos
 caracteres de formatação.
"""


cpf = input(': ')
numbers = [int(digit) for digit in cpf if digit.isdigit()]

soma_dos_produtos1 = (sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1))))
soma_dos_produtos2 = (sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1))))
digito_verificador1 = str((soma_dos_produtos1 * 10) % 11)
digito_verificador2 = str((soma_dos_produtos2 * 10) % 11)
print(digito_verificador1, digito_verificador2)
print(cpf[12], cpf[13])

if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    if len(cpf) == 14:
        if cpf[12] == digito_verificador1 and cpf[13] == digito_verificador2:
            print('O cpf é válido')
        else:
            print('O cpf possui os digitos validadores inválidos')
    else:
        print('O cpf precisa ter 14 caracteres.')


else:
    print('Cpf inválido, digite a formatação correta.')

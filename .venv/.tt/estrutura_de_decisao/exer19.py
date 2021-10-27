"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades

12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

numero = int(input('adicione um numero: '))

centenas_str = dezenas_str = unidades_str = ''

centenas_int, numero = divmod(numero, 100)
if centenas_int == 1:
    centenas_str = '1 centena'
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'


dezenas_int, numero = divmod(numero, 10)
if dezenas_int == 1:
    dezenas_str = '1 dezena'
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'


if numero == 1:
    print('1 unidade')
elif numero > 1:
    print(f'{numero} unidades')

print(centenas_str, dezenas_str, unidades_str)

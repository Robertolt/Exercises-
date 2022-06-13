"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do
usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

data = input('Data de Nascimento(XX/ZZ/YYYY): ')
numero_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
              'Setembro', 'Outubro', 'Novembro', 'Dezembro']


print(f'Você nasceu em', data.split("/")[0], f'de {numero_mes[int(data.split("/")[1])-1]} de', data.split("/")[2])

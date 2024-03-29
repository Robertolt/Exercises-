"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos
vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
"""

salarios = [201,240, 350, 490, 550, 650, 798, 800, 905, 1000, 2000, 3000]
contagem_de_faixa_salarial = [0]*9
for salario in salarios:
    indice = salario // 100 - 2
    indice_maximo = len(contagem_de_faixa_salarial) - 1
    indice = min(indice, indice_maximo)
    contagem_de_faixa_salarial[indice] += 1

print(contagem_de_faixa_salarial)

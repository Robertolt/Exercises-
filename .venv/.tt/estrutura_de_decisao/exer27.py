"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

kg_morango = float(input('Digite quantos Kg de morangos você irá comprar: '))
kg_banana = float(input('Digite quantos Kg de banana você irá comprar: '))

if kg_morango > 5:
    if kg_morango > 8:
        print('Você pagará: R$', (kg_morango*2.20)*0.9, f' e levará {kg_morango}kg de morango')
    else:
        print('Você pagará: R$', (kg_morango*2.20), f' e levará {kg_morango}kg de morango')
else:
    print('Você pagará: R$', (kg_morango * 2.50), f' e levará {kg_morango}kg de morango')

if kg_banana > 5:
    if kg_banana > 8:
        print('Você pagará: R$', (kg_banana*1.50)*0.9, f' e levará {kg_banana}kg de banana')
    else:
        print('Você pagará: R$', (kg_banana*1.50), f' e levará {kg_banana}kg de banana')
else:
    print('Você pagará: R$', (kg_banana * 1.80), f' e levará {kg_banana}kg de banana')

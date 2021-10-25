"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;
-misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
 valores para cima,isto é, considere latas cheias."""


sm = float(input('size in square meters that needs to be painted: '))
sm = sm*1.1

if sm <= 108:
    print('1 tin of 18l is needed and u will pay 80R$')
else:
    if sm %108 != 0:
        print((sm//108) +1, 'tins of 18l is needed and u will pay ', int((sm//108) +1)*80, 'R$')

if sm <= 21.6:
    print('1 tin of 3.6l is needed and u will pay 25R$')
else:
    if sm %21.6 != 0:
        print((sm//21.6) +1, 'tins of 3.6l is needed and u will pay ', int((sm//21.6) +1)*25, 'R$')

if sm < 108:
    print((sm//21.6) +1, 'tins of 3.6l is needed and u will pay ', int((sm//21.6) +1)*25, 'R$')
elif sm == 108:
    print('1 tin of 18l is needed and u will pay 80R$')
elif sm > 108:
    if sm %108 !=0:
        print(sm//108, 'tins of 18l and', ((sm%108)//21.6) + 1,'tins of 3.6l and u will pay',
              int((sm//108)*80 + (sm%108//21.6) +1) ,'R$')

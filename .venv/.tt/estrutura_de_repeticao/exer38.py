"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
 Faça um programa que determine o salário atual desse funcionário. Após concluir isto,
 altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

taxa_aumento = 1.015
salario_inicial = 1000
ano_inicial = 1996
tempo_trabalhado = 2022 - ano_inicial

for _ in range(tempo_trabalhado):
    salario_inicial = salario_inicial*taxa_aumento
    taxa_aumento += 0.01
    print(salario_inicial)

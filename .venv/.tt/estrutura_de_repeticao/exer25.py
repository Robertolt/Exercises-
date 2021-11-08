"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
 turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
 conforme a média calculada."""

qntd_pessoas = int(input('informe a quantidade de pessoas: '))
soma = 0

for n in range(1, qntd_pessoas + 1):
    soma += float(input('Insira as idades: '))
    media = soma / n
    if media <= 25:
        faixa_etaria = 'jovem'
    elif 26 <= media < 60:
        faixa_etaria = 'adulta'
    else:
        faixa_etaria = 'idosa'
    print(f'a média aritmética das idades é {media}, logo a turma é {faixa_etaria}')

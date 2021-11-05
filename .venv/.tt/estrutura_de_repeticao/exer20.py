"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
 fatorial a números inteiros positivos e menores que 16.""" # 0 <= x <=16

while True:
    while True:
        fatorial = int(input('input a number: '))#5*4*3*2*1
        primeiro = 1
        numero = 1

        if 0 <= fatorial <= 16:
            for _ in range(fatorial):
                numero *= primeiro
                primeiro += 1
            print(numero)
            break
        else:
            print('coloque numeros entre 0 e 16 para o fatorial')

    variavel_de_final = str(input('Deseja calcular algum fatorial novamente(y/n) ?: '))
    if variavel_de_final == 'n':
        break
    else:
        pass

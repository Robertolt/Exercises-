"""Uma academia deseja fazer um senso entre seus clientes para
descobrir o mais alto, o mais baixo, a mais gordo e o
mais magro, para isto você deve fazer um programa que pergunte a
cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada
quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e
valores do clente mais alto, do mais baixo, do mais gordo
 e do mais magro, além da média das alturas e dos pesos dos clientes"""

cod_client = []
altura = []
peso = []
n_cliente = 0

while True:
    cod_client.append(int(input('insira seu código: ')))
    if cod_client == 0:
        break
    else:
        altura = float(input('insira sua altura: '))
        peso = float(input('insira seu peso: '))
        n_cliente += 1

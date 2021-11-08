"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

qntd_turmas = int(input('Digite a quantidade de turmas: '))
soma = 0

for n in range(1, qntd_turmas + 1):  #0 e terminaria no N-1, onde N é o número de entrada informado pelo o user

    while True:

        num_alunos_turma = int(input('Digite a quantidade de alunos em cada turma: '))
        if num_alunos_turma > 40:
            print('As turmas deverão ter menos que 40 alunos')
        else:
            break

    soma += num_alunos_turma
    media = soma/n
    print(f'o número de alunos por turma na média é de {media}')

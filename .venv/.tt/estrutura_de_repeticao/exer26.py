"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
 votar e ao final mostrar o número de votos de cada candidato."""

n_votantes = int(input('quantas pessoas irão votar: '))
candidato_A = 0
candidato_B = 0
candidato_C = 0

for _ in range(n_votantes):
    voto_do_eleitor = str(input('Para votar no candidato A, vote(a), no condidato B, vote(b), no candidato C, vote(c): '))
    voto_do_eleitor = voto_do_eleitor.upper()

    if voto_do_eleitor == 'A':
        candidato_A += 1
    elif voto_do_eleitor == 'B':
        candidato_B += 1
    elif voto_do_eleitor == 'C':
        candidato_C += 1
    else:
        print('Voto inválido')

<<<<<<< HEAD
=======
print(f'o cantidato A teve {candidato_A} votos, o candidato B teve {candidato_B}, e o candidato C teve {candidato_C} votos')
>>>>>>> feito os 4 primeiros exercicios de sequencias de repeticao

"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

lista = []
N_numeros = int(input('coloque a quantidade de números desejada: '))

for _ in range(N_numeros):
    numeros_adicionados = (int(input('digite os números desejados entre 0 e 1000: ')))
    if 0 <= numeros_adicionados <= 1000:
        lista.append(numeros_adicionados)

if max(lista) == min(lista):
    print('o numero é', max(lista), 'e a soma é', sum(lista))
else:
    print('o número máximo é', max(lista), 'o número mínimo é', min(lista), 'a soma é', sum(lista))

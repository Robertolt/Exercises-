"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando
a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
"""

lista = []
qnt_valores_lidos = 0

while True:
    nota = float(input('Insira a nota desejada (Para encerrar digite "-1"): '))
    if nota == -1:
        break
    else:
        lista.append(nota)
        qnt_valores_lidos += 1


print(f'Foram lidos {qnt_valores_lidos} valor(es)')


print(' '.join([str(numero) for numero in lista]))


lista.reverse()
for numero in lista:
    print(numero)


print('A soma das notas foi: ')
print(sum(lista))


print('A média das notas foi: ')
media = sum(lista)/qnt_valores_lidos
print(media)


print('Notas acima da média: ')
print(' '.join([str(numero) for numero in lista if numero > media]))


print('Notas abaixo de 7: ')
print(' '.join([str(numero) for numero in lista if numero < 7]))



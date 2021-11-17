"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
 indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
 temperaturas."""

lista = []
divisor = 0

while True:
    try:
        temp = int(input('Insira as temperaturas desejadas (para encerar digite "end"): '))
    except ValueError:
        break
    else:
        lista.append(temp)
        divisor += 1

print(f'a menor temperatura foi {min(lista)}, a maior foi {max(lista)} e a média foi {sum(lista)/divisor}')

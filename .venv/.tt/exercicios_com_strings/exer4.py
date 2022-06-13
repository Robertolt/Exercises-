"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

nome = 'roberto'.upper()
lista_letras = list(nome)
print(lista_letras)

for i in range(len(nome)):
    for k in range(0, i + 1):
        print(lista_letras[k], end='')
    print(end='\n')

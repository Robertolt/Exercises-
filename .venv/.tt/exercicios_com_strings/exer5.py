"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F

"""

nome = 'roberto'.upper()
lista_letras = list(nome)
print(lista_letras)

for i in range(len(nome), 0, - 1):
    for k in range(i):
        print(lista_letras[k], end='')
    print(end='\n')

# Outra forma de resolução

s = 'FULANO'
while s != '':
    print(s)
    s = s[:-1]

"""Develop a program witch verifies if the written letter is F ou M. According to the letter, the program should return
(F)emale, (M)ale or Invalid"""

"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - 
Masculino, Sexo Inválido."""

gender = input('Type on a letter for the gender: ').upper()
if gender == 'M':
    print('MALE')
elif gender == 'F':
    print('Female')
else:
    print('Invalid')

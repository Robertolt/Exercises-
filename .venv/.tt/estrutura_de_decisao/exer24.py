"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

classification = 0
y = 1
n = 0
a1 = a2 = a3 = a4 = a5 = 1

a1 = str(input('Called the victim?(y/n): '))
if a1 == 'y':
    classification += 1
else:
    pass

a2 = str(input('Have you been in the crime scene?(y/n): '))
if a2 == 'y':
    classification += 1
else:
    pass

a3 = str(input("Live close to the victim's house?(y/n): "))
if a3 == 'y':
    classification += 1
else:
    pass

a4 = str(input("Owned money to the victim?(y/n): "))
if a4 == 'y':
    classification += 1
else:
    pass

a5 = str(input("Have you worked with the victim?(y/n): "))
if a5 == 'y':
    classification += 1
else:
    pass

if classification < 2:
    print('innocent')
elif classification == 2:
    print('suspect')
elif classification == 5:
    print('guilty')
else:
    print('accomplice')
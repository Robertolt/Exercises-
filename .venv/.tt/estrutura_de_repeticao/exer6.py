"""Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
 ele mostre os números um ao lado do outro."""

number_list = range(21)

for i in number_list:
    print(i)
    print(list(range(i)))

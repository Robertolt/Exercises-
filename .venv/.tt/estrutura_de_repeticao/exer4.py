"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento."""

popA = 80_000
popB = 200_000
year = 0

while popA <= popB:
    popA = popA*1.03
    popB = popB*1.015
    year += 1

print(year)

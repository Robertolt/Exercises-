"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

size = float(input('input the size of the file: '))
speed = float(input('input the internet speed: '))
time = (size/speed)/60
print('the download takes ', time, ' minutes')


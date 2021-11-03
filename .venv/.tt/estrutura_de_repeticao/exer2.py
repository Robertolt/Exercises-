"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""

while True:
    name = input('Input your username: ')
    password = input('Input your password: ')

    if name == password:
        print('ERROR: NAME AND PASSWORD NEED TO BE DIFERENT')
    else:
        print('please, be welcome')
        break

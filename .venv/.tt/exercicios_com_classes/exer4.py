"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
 sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self, acrescimo_peso):
        self.peso = self.peso + acrescimo_peso

    def emagrecer(self, decrescimo_peso):
        self.peso = self.peso - decrescimo_peso


pessoa = Pessoa('Roberto', 10, 100, 170)


for _ in range(22):
    pessoa.envelhecer()
    pessoa.engordar(1)
    print(f'O nome da pessoa é {pessoa.nome}, a idade é de {pessoa.idade} anos,'
          f' o peso é de {pessoa.peso}Kg e a sua altura é {pessoa.altura}cm')

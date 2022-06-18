"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, tamanho_do_lado=1):
        self.tamanho_do_lado = tamanho_do_lado

    def calcular_area(self):
        return self.tamanho_do_lado ** 2


quadrado = Quadrado(4)
print(quadrado.tamanho_do_lado, quadrado.calcular_area())

"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Borracha'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor


bola_um = Bola()
bola_dois = Bola()
bola_dois.troca_cor('Amarelo')

print(bola_um.mostra_cor(), bola_dois.cor)

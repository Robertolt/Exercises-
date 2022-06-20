"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:

abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros
 que foi colocada no veículo

abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível
e mostra o valor a ser pago pelo cliente.

alterarValor( ) – altera o valor do litro do combustível.

alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecer: float):
        if (valor_abastecer / self.valor_litro) > self.quantidade_combustivel:
            print(f'Falta {valor_abastecer / self.valor_litro - self.quantidade_combustivel:.2f}' 
                  'litros para completar o abastecimento', end='\n'
                  'Por favor, abasteça a bomba \n\n')
        else:
            print(f'Foram abastecidos: {(valor_abastecer / self.valor_litro):.2f} '
                  f'litros a um valor de R$ {self.valor_litro}', end='\n')
            self.quantidade_combustivel -= valor_abastecer / self.valor_litro
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros\n')

    def abastecer_por_litros(self, litros: float):
        if litros > self.quantidade_combustivel:
            print(f'Falta {(litros - self.quantidade_combustivel):.2f} litros para completar o abastecimento', end='\n'
                  'Por favor, abasteça a bomba \n\n')
        else:
            print(f'Foram abastecidos: {litros} '
                  f'litros a um valor de R$ {litros * self.valor_litro}')
            self.quantidade_combustivel -= litros
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros\n')

    def alterar_valor(self, valor_combustivel: float):
        self.valor_litro = valor_combustivel
        print(f'O preço do combustível foi atualizado para R${self.valor_litro} por Litro\n ')

    def alterar_quantidade_combustivel(self, litros_adicionados: float):
        if litros_adicionados <= 0:
            print('É impossível retirar combustível dessa bomba sem abastecer!')
        else:
            self.quantidade_combustivel += litros_adicionados
            print(f'Foram adicionados a bomba {litros_adicionados} litros e agora há um total de '
                  f'{self.quantidade_combustivel:.2f} litros')


bomba = BombaCombustivel('Gasolina', 7.00, 100.0)
bomba.abastecer_por_valor(100), bomba.abastecer_por_litros(90), bomba.alterar_valor(7.50)
bomba.abastecer_por_litros(20), bomba.alterar_quantidade_combustivel(100)

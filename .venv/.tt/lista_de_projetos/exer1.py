lista_de_dados = []


def transformar_em_megabytes(tamanho_em_bytes: str) -> float:
    return int(tamanho_em_bytes) / (2 ** 10) ** 2


with open('/home/robertolt/PycharmProjects/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((tamanho_em_disco, usuario))

quantos_users = int(input('digite quantos usuarios voce quer ver: '))
lista_de_dados.sort(reverse=True)
lista_de_dados = lista_de_dados[:quantos_users]


with open('/home/robertolt/PycharmProjects/relatorio.txt', 'w') as arquivo:
    tamanho_total_consumido = sum([tamanho for tamanho, _ in lista_de_dados])
    arquivo.writelines(
        'ACME Inc.               Uso do espaço em disco pelos usuários\n'
        '------------------------------------------------------------------------\n'
        'Nr.  Usuário        Espaço utilizado             % do uso\n\n')

    for indice, dados in enumerate(lista_de_dados, start=1):
        tamanho_em_disco, usuario = dados
        arquivo.writelines(
            f'{indice:<4}    {usuario} {tamanho_em_disco:9.2f} MB             '
            f'{tamanho_em_disco/tamanho_total_consumido:>6.2%}\n')
    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {tamanho_total_consumido/len(lista_de_dados):.2f} MB\n')

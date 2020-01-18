print('Controle de Terrenos')
print('=' * 30)


def calculaArea(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m².')


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
calculaArea(largura, comprimento)

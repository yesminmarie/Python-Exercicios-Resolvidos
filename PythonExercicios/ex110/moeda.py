def resumo(preco=0, taxaAumento=10, taxaReducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Metade do preço: \t{metade(preco, True):>10}')
    print(f'Dobro do preço: \t{dobro(preco, True):>10}')
    print(f'{taxaAumento} de aumento: \t\t{aumentar(preco, taxaAumento, True):>10}')
    print(f'{taxaReducao} de redução: \t\t{diminuir(preco, taxaReducao, True):>10}')
    print('-' * 30)


def metade(preco=0, formatado=False):
    res = preco /2
    return res if formatado is False else moeda(res)


def dobro(preco=0, formatado=False):
    res = preco * 2
    return res if formatado == False else moeda(res)


def aumentar(preco=0, taxa=0, formatado=False):
    res = preco + (preco * taxa/100)
    return res if not formatado else moeda(res)


def diminuir(preco=0, taxa=0, formatado=False):
    res = preco - (preco * taxa/100)
    return res if not formatado else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

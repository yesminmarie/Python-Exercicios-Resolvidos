print('=' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('=' * 30)
total = maisDeMil = precoMaisBarato = cont = 0
prodMaisBarato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maisDeMil += 1
    if cont == 1 or preco < precoMaisBarato:
        precoMaisBarato = preco
        prodMaisBarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodMaisBarato} que custa R${precoMaisBarato:.2f}')

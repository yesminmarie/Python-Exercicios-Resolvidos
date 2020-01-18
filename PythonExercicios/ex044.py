print('{:=^40}'.format(' LOJAS LAHOUD '))
preco = float(input('Preço da compra: R$'))
print('''FORMAS DE PAGAMENTO:'
      [1] à vista dinheiro/cheque: 10% de desconto
      [2] à vista no cartão: 5% de desconto
      [3] em até 2x no cartão: preço normal
      [4] 3x ou mais no cartão: 20% de juros''')
condicaoPagamento = int(input('Qual é a opção? '))
if condicaoPagamento == 1:
    precoFinal = preco - (preco*0.1)
elif condicaoPagamento == 2:
    precoFinal = preco - (preco*0.05)
elif condicaoPagamento == 3:
    precoFinal = preco
    parcela = precoFinal / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif condicaoPagamento == 4:
    precoFinal = preco + (preco*0.2)
    quantParcelas = int(input('Quantas parcelas?'))
    parcela = precoFinal / quantParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(quantParcelas, parcela))
else:
    precoFinal = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, precoFinal))

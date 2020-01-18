preco = float(input('Digite o preço do produto: R$'))
# desconto de 5%
novo = preco - preco*0.05
print('O novo valor com desconto é R${:.2f}'.format(novo))
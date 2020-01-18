km = float(input('Quantidade de Km percorridos: '))
dias = int(input('Quantidade de dias que o carro foi alugado: '))
#o carro custa R$60,00 por dia e R$0,15 por Km rodado
preco = dias*60 + km*0.15
print('Seu carro percorreu {}Km em {} dias. O total a pagar é de R${:.2f}'.format(km, dias, preco))
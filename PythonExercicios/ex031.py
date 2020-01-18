distancia = float(input('Qual a distância em Km?'))
if distancia <= 200:
    print('O valor da passagem é R${}'.format(distancia * 0.5))
else:
    print('O valor da passagem é R${:.2f}'.format(distancia * 0.45))

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((velocidade-80)*7))
print('Tenha um bom dia! Dirija com segurança!')
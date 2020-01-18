print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
resto = 0
maiorCedula = 50
while True:
    if valor < 10:
        maiorCedula = 1
    elif valor < 20:
        maiorCedula = 10
    elif valor < 50:
        maiorCedula = 20
    cedulas = valor // maiorCedula
    if cedulas == 0:
        break
    print(f'Total de {cedulas} cédulas de R${maiorCedula}')
    resto = valor % maiorCedula
    valor = resto
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


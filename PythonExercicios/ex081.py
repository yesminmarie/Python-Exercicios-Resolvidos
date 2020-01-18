valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resp in 'n':
        break
valores.sort(reverse=True)
print('-=' * 40)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

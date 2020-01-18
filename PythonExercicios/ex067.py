while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if t < 0:
        break
    for cont in range(1, 11):
        print(f'{t} x {cont} = {t*cont}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
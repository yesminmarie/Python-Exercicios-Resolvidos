numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {numeros[n]}.')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
print('{:=^30}'.format(' FIM DO PROGRAMA! '))



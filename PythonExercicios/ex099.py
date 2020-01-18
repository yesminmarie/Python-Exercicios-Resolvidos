from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    if len(num) != 0:
        maior = num[0]
        for n in num:
            if n > maior:
                maior = n
            print(f'{n} ', end='')
            sleep(0.3)
    else:
        maior = 0
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()

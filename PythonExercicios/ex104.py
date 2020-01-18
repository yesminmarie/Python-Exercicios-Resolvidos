def leiaInt(texto):
    ok = False
    valor = 0
    while True:
        num = str(input(texto))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

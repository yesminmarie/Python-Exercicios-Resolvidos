from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 30)
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -passo
        fim -= 1
    if inicio < fim:
        fim += 1
    for c in range(inicio, fim, passo):
        sleep(0.5)
        print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:   '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


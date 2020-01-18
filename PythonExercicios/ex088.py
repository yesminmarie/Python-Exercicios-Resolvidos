from random import randint
from time import sleep
print('=' * 30)
print('{:^30}'.format('JOGA NA MEGA SENHA'))
print('=' * 30)
jogos = []
temp = []
sorteios = int(input('Quantos jogos você quer que eu sorteie? '))
for cont in range(1, sorteios+1):
    c = 1
    while c <= 6:
        numero = randint(1, 60)
        if numero not in temp:
            temp.append(numero)
            c += 1
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
print('-=' * 3, f' SORTEANDO {sorteios} JOGOS ', '-=' * 3)
for cont, j in enumerate(jogos):
    print(f'Jogo {cont+1}: {j}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)



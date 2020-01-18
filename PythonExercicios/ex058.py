from random import randint
tentativas = 0
computador = randint(0, 10)
acertou = False
print('='*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('='*20)
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais..Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))

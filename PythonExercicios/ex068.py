from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('=' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. ', end='')
    print('Deu PAR.' if soma % 2 == 0 else 'Deu ÍMPAR.')
    if soma % 2 == 0:
        print('=' * 30)
        if tipo == 'P':
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print('=' * 30)
        if tipo == 'P':
            print('Você PERDEU!')
            break
        else:
            print('Você VENCEU!')
            cont += 1
    print('Vamos jogar novamente...')
    print('=-' * 30)
print('=-' * 30)
print(f'GAME OVER! Você venceu {cont} vezes.')


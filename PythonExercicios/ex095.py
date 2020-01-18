lista = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    partidas.clear()
    print('=' * 30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for cont in range(0, quant):
        partidas.append(int(input(f'   Quantos gols na partida {cont+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(jogador['gols'])
    lista.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
#cabeçalho (o dicionário jogador terá apenas os dados do último jogador)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<16}', end='')
print()
print('-' * 40)
for pos, e in enumerate(lista):
    print(f'{pos:>3} ', end='') # imprime a posição de cada dicionário
    for v in e.values(): # imprime os valores de cada dicionário
        print(f'{str(v):<15}', end=' ')
    print()
print('-' * 40)
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break
    if cod >= len(lista):
        print(f'ERRO! Não existe jogador com código {cod}! Tente novamente.')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {lista[cod]["nome"]}:')
        for pos, g in enumerate(lista[cod]['gols']):
            print(f'   No jogo {pos+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')





jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, quant):
    partidas.append(int(input(f'   Quantos gols na partida {cont}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(jogador['gols'])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

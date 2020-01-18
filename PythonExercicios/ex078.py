valores = []
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {pos}: ')))
print('=-' * 40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if max(valores) == v:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if min(valores) == v:
        print(f'{pos}...', end=' ')

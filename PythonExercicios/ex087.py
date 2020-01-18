matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTercCol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
        if coluna == 2:
            somaTercCol += matriz[linha][2]
    print()
print('-=' * 40)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTercCol}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

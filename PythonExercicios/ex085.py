numeros = [[], []]
for cont in range(1, 8):
    num = int(input(f'Digite o {cont}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')

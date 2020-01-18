valores = list()
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        for pos in range(0, len(valores)):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
print('-=' * 40)
print(f'Os valores digitados em ordem foram {valores}')


soma = 0
cont = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma entre todos os {} números ímpares que são múltiplos de três é: {}'.format(cont, soma))
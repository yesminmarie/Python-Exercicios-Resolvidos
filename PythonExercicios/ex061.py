print('Gerador de PA')
print('-='*10)
primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 1
termo = primeiroTermo
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1
print('Acabou')

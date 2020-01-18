primeiroTermo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimoTermo = primeiroTermo + (10 - 1) * razao
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
for c in range(primeiroTermo, decimoTermo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')

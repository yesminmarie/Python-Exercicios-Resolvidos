n = int(input('Digite um número para ver sua tabuada: '))
print('='*20)
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n, c, c*n))
print('='*20)
print('FIM')
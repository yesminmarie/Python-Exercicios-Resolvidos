r1 = int(input('Digite o comprimento da 1ª reta: '))
r2 = int(input('Digite o comprimento da 2ª reta: '))
r3 = int(input('Digite o comprimento da 3ª reta: '))
if abs(r2-r3) < r1 < r2+r3 and abs(r1-r3) < r2 < r1+r3 and abs(r1-r2) < r3 < r1+r2:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')
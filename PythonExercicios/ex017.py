import math
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = math.sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
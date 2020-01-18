s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if abs(s2-s3) < s1 < s2+s3 and abs(s1-s3) < s2 < s1+s3 and abs(s1-s2) < s3< s1+s2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO.')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos acima NÂO podem formar um triângulo!')

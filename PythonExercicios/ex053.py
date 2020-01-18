frase = str(input('Digite uma frase: ')).strip().upper()
fraseSplit = frase.split()
fraseJoin = ''.join(fraseSplit)
fraseContrario = ''
#solução sem for
fraseContrario = fraseJoin[::-1]
#for letra in range(len(fraseJoin)-1, -1, -1):
    #fraseContrario += fraseJoin[letra]
print('O inverso de {} é {}'.format(fraseJoin, fraseContrario))
if fraseJoin == fraseContrario:
    print('A frase {} é um PALÍNDROMO'.format(frase))
else:
    print('A frase {} NÂO é um PALíNDROMO'.format(frase))

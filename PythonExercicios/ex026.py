frase = str(input('Digite uma frase: ')).strip()
print('A letra "a" aparece {} vezes.'.format(frase.lower().count('a')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.lower().find('a')+1))
print('A última letra "a" apareceu na posição {}'.format(frase.lower().rfind('a')+1))

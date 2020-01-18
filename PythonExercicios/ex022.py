nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras, sem considerar espaços.'.format(len(nome) - nome.count(' ')))
#procura pelo primeiro espaço e mostra a posição deste espaço
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

#minha solução
#nome = input('Digite seu nome completo: ')
#print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
#print('Seu nome em minúsculas: {}'.format(nome.lower()))
#nome_split = nome.split()
#nome_join = ''.join(nome_split)
#print('Seu nome tem {} letras, sem considerar espaços.'.format(len(nome_join)))
#print('Seu primeiro nome tem {} letras.'.format(len(nome_split[0])))

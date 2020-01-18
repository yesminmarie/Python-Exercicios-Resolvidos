somaIdade = 0
mediaIdade = 0
idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ''
mulheresMenos20Anos = 0
for p in range(1, 5):
    print('='*5, end='')
    print('{}ª PESSOA'.format(p), end='')
    print('='*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if sexo in 'Mm' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresMenos20Anos += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é {}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeHomemMaisVelho, nomeHomemMaisVelho))
print('Há {} mulheres com idade menor que 20 anos'.format(mulheresMenos20Anos))

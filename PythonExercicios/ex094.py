lista = []
pessoa = {}
media = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
media = soma/len(lista)
print('-=' * 30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for e in lista:
    if e['sexo'] == 'F':
        print(e['nome'], end=' ')
print('\n- Lista das pessoas que estão acima da média: ')
for e in lista:
    if e['idade'] >= media:
        print('     ', end='')
        for k, v in e.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')

print('=' * 30)
print('CADASTRE UMA PESSOA')
print('=' * 30)
maior18 = homem = mulherMenor20 = 0
while True:
    sexo = continuar = ' '
    idade = int(input('Idade: '))
    if idade >= 18:
        maior18 += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulherMenor20 += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulherMenor20} mulheres com menos de 20 anos.')
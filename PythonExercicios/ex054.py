from datetime import date
contMaior = 0
contMenor = 0
for c in range(1, 8):
    anoNasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - anoNasc >= 21:
        contMaior += 1
    else:
        contMenor += 1
print('{} pessoas ainda não atingiram a maioridade e {} já são maiores.'.format(contMenor, contMaior))
from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
idade = anoAtual - anoNasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JÚNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')
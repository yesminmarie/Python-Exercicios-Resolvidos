from datetime import date
anoNascimento = int(input('Informe o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
tempoAlistamento = abs(18-idade)
print('Quem nasceu em {} tem {} anos em {}'.format(anoNascimento, idade, anoAtual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.'.format(tempoAlistamento, anoAtual+tempoAlistamento))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(tempoAlistamento, anoAtual-tempoAlistamento))
else:
    print('Você tem que se alistar IMEDIATAMENTE')


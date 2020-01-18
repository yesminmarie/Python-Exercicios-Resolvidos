from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - anoNasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - anoNasc
print('-=' * 30)
for k, v in pessoa.items():
    print(f' -{k} tem o valor {v}')


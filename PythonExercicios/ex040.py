n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média é {:.2f}'.format(media))
if media < 5:
    print('O aluno está REPROVADO.')
elif 5 <= media < 7:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está APROVADO.')
alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? ')).strip().lower()[0]
    if resp == 'n':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 30)
for pos in range(0, len(alunos)):
    print(f'{pos:<3} {alunos[pos][0]:<10} {alunos[pos][2]:>6.1f}')
print('=' * 30)
while True:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp == 999:
        break
    if resp <= len(alunos)-1:
        print(f'Notas de {alunos[resp][0]} são {alunos[resp][1]}')
    print('=' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
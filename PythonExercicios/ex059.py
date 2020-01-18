from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = 0
multiplic = 0
maior = 0
opcao = 0
while opcao != 5:
    print('''Escolha uma opção: 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplic = n1 * n2
        print('O produto entre {} e {} é: {}'.format(n1, n2, multiplic))
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('O maior número entre {} e {} é: {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

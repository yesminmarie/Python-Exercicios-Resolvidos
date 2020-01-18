n = int(input('Digite um número inteiro:'))
print('''Escolha a base de conversão 
    \033[34m 1\033[m converter para\033[33m binário\033[m
    \033[34m 2\033[m converter para\033[33m octal\033[m
    \033[34m 3\033[m converter para\033[33m hexadecimal\033[m''')
opcao = int(input('Sua opção: '))
#[2:] da posição 2 até o final (para tirar os códigos das bases)
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')

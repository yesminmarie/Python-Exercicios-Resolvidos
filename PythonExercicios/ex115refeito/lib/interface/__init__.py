def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '=' * tam


def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[32m{cont} -\033[m \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

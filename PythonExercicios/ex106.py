from time import sleep
c = ('\033[m',       # 0 - sem cores
     '\033[30;42m',  # 1 - verde
     '\033[30;44m',  # 2 - azul
     '\033[7;30m',   # 3 - branco
     '\033[30;41m'   # 4 - vermelho
    )


def escreva(texto, cor=0):
    tam = len(texto) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {texto}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.5)


def exibeManual(cmd):
    escreva(f'Acessando o manual do comando \'{cmd}\'', 2)
    print(c[3], end='')
    help(cmd)
    print(c[0], end='')
    sleep(0.5)


while True:
    escreva('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > ')).lower().strip()
    if comando == 'fim':
        break
    exibeManual(comando)
escreva('ATÉ LOGO!', 4)

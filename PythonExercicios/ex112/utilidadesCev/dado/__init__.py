def leiaDinheiro(msg):
    while True:
        preco = str(input(msg)).replace(',', '.').strip()
        if preco.isalpha() or preco == '':
            print(f'\033[31mERRO: \"{preco}\" é um preço inválido\033[m')
        else:
            return float(preco)
            break


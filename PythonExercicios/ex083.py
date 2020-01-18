expr = str(input('Digite a expressão: '))
lista = []
for simb in expr:
    # se encontrar o '(' ele é adicionado à lista
    if simb == '(':
        lista.append('(')
    # se encontrar o ')' e a lista não estiver vazia, o último elemento é removido
    # ou seja, se encontrar o par, o elemento é removido
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        # se a lista estiver vazia, o ')' será adicionado à ela, significando que o par não foi encontrado
        #e sai do loop
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

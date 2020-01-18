from ex115refeito.lib.interface import *
from ex115refeito.lib.arquivo import *
from time import sleep

arq = 'CursoEmVideo.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema...Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
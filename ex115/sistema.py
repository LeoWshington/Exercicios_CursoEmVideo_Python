from time import sleep

from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menuprincipal(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opcao == 1:
        # Listar o conteudo de um arquivo
        lerArquivo(arq)
    elif opcao == 2:
        cabecalho('Novo Cadastro')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mErro digite um opção valida!\033[m')
    sleep(2)

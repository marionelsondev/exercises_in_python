from time import sleep
from lib.interface import menu, cabecalho, leiaInt
from lib.db import arquivo_existe, criar_arquivo_db, listar_pessoas, cadastrar_pessoa


arquivo_db = 'cursoemvideo.txt'

if not arquivo_existe(arquivo_db):
    criar_arquivo_db(arquivo_db)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        listar_pessoas(arquivo_db)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar_pessoa(arquivo_db, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

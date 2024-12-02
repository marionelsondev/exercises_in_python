from time import sleep
from lib.interface import cabecalho


def arquivo_existe(nome_arquivo):
    try:
        arquivo_db = open(nome_arquivo, 'rt')
        arquivo_db.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo_db(nome_arquivo):
    try:
        arquivo_db = open(nome_arquivo, 'wt+')
        arquivo_db.close()
    except:
        print(f'\033[0;31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!')


def listar_pessoas(nome_arquivo):
    try:
        arquivo_db = open(nome_arquivo, 'r')
    except:
        print('\033[0;31mErro ao ler arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        sleep(1)
        print(arquivo_db.read())

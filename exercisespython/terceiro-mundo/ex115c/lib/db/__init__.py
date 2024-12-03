from time import sleep
from lib.interface import cabecalho, leiaInt


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
        arquivo_db = open(nome_arquivo, 'rt')
    except:
        print('\033[0;31mErro ao ler arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arquivo_db:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo_db.close()


def cadastrar_pessoa(nome_arquivo, nome='desconhecido', idade=0):
    try:
        arquivo_db = open(nome_arquivo, 'at')
        arquivo_db.write(f'\n{nome};{idade}')
        print(f'Novo registro de {nome} adicionado.')
    except:
        print('\033[0;31mOcorreu um erro a tentar cadastrar uma nova pessoa\033[m')
    finally:
        arquivo_db.close()

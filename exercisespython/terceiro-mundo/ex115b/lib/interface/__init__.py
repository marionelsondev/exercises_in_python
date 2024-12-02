def leiaInt(prompt):
    """
    Valida se o número digitado é um número inteiro

    Args:
        prompt (str): Mensagem do input
    """
    while True:
        try:
            nint = int(input(prompt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return nint


def linha(tam=42):
    return tam*'-'


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    cabecalho('MENU PRINCIPAL')
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[0;33mSua Opção: \033[m')
    print(opcao)
    return opcao

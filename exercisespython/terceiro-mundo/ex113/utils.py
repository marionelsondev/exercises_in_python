def leiaInt(prompt):
    """
    Valida se o número digitado é um número inteiro

    Args:
        prompt (str): Mensagem do input
    """
    while True:
        try:
            nint = int(input(prompt))
            if nint:
                break
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        return nint


def leiaFloat(prompt):
    """
    Valida se o número digitado é um número real

    Args:
        prompt (str): Mensagem do input
    """
    while True:
        try:
            nfloat = float(input(prompt))
            if nfloat:
                break
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        return nfloat

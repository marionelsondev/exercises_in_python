def moeda(preco=0, moeda='R$'):
    """
    -> Retorna o valor formatado como moeda.
    :param preco: valor a ser formatado.
    :param moeda: moeda a ser utilizada.
    :return: valor formatado como moeda.
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def metade(preco=0, formatar=False):
    """
    -> Retorna a metade do valor.
    :param preco: valor a ser calculado.
    :param formatar: formata o valor como moeda.
    :return: metade do valor.
    """
    res = preco / 2
    return res if not formatar else moeda(res)


def dobro(preco=0, formatar=False):
    """
    -> Retorna o dobro do valor.
    :param preco: valor a ser calculado.
    :param formatar: formata o valor como moeda.
    :return: dobro do valor.
    """
    res = preco * 2
    return res if not formatar else moeda(res)


def aumentar(preco=0, taxa=0, formatar=False):
    """
    -> Retorna o valor com aumento.
    :param preco: valor a ser calculado.
    :param taxa: taxa de aumento.
    :param formatar: formata o valor como moeda.
    :return: valor com aumento.
    """
    res = preco * (1 + taxa / 100)
    return res if not formatar else moeda(res)


def diminuir(preco=0, taxa=0, formatar=False):
    """
    -> Retorna o valor com redução.
    :param preco: valor a ser calculado.
    :param taxa: taxa de redução.
    :param formatar: formata o valor como moeda.
    :return: valor com redução.
    """
    res = preco * (1 - taxa / 100)
    return res if not formatar else moeda(res)


def resumo(preco=0, aumento=10, reducao=5):
    """
    -> Retorna um resumo do valor.
    :param preco: valor a ser calculado.
    :param aumento: taxa de aumento.
    :param reducao: taxa de redução.
    """
    print(32*'-')
    print('RESUMO DO VALOR'.center(32))
    print(32*'-')
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t\t{diminuir(preco, reducao, True)}')
    print(32*'-')

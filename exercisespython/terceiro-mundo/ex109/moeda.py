def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def metade(preco=0, formatar=False):
    res = preco / 2
    return res if not formatar else moeda(res)

def dobro(preco=0, formatar=False):
    res = preco * 2
    return res if not formatar else moeda(res)

def aumentar(preco=0, porcentagem=0, formatar=False):
    res = preco * (1 + porcentagem / 100)
    return res if not formatar else moeda(res)

def diminuir(preco=0, porcentagem=0, formatar=False):
    res = preco * (1 - porcentagem / 100)
    return res if not formatar else moeda(res)

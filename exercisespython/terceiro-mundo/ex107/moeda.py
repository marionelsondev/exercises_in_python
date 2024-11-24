def metade(preco):
    return preco / 2

def dobro(preco):
    return preco * 2

def aumentar(preco, porcentagem):
    preco_aumentado = preco * (1 + porcentagem / 100)
    return preco_aumentado

def diminuir(preco, porcentagem):
    preco_reduzido = preco * (1 - porcentagem / 100)
    return preco_reduzido

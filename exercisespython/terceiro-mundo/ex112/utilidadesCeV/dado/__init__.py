def leiaDinheiro(prompt=''):
    valido = False
    while not valido:
        p = str(input(prompt).strip().replace(',', '.'))
        if p.isalpha() or p == '':
            print(f'\033[0;31mERRO: "{p}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(p)

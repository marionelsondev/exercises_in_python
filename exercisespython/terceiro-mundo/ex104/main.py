def leiaInt(prompt=''):
    while True:
        ok = False
        valor = 0
        n = str(input(prompt))
        if n.isdigit():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

print(30*'-')
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

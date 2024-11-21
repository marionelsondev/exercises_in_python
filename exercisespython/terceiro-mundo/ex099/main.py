from time import sleep

def maior(*num):
    cont = maior = 0
    print(24*'-=')
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:   
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(11, 3, 5, 24, 13, 30)
maior(99, 102, 1, 53, 45)
maior(7, 4, 2)
maior(8)
maior()
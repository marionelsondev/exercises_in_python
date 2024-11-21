from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0, 100)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista} temos {soma}.')

numeros = []
sorteia(numeros)
somaPar(numeros)

from random import randint
from time import sleep

num_jogos = 0
lista = []
jogo = []

print(24*'-')
print(f'{4*' '}JOGA NA MEGA SENA')
print(24*'-')

num_jogos = int(input(f'Quantos jogos você quer que eu sorteie? '))
print(f'{3*'-='} SORTEANDO {num_jogos} JOGOS {3*'-='}')

for g in range(0, num_jogos):
    for n in range(6):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    sleep(0.3)
    print(f'Jogo {g+1}: {jogo[g]}')

print(f'{5*'-='} < BOA SORTE! > {5*'-='}')

from random import randint
from time import sleep

jogos = {}
ranking = []
contador = 1

print('Valores sorteados:')
for p in range(1, 5):
    jogos[f'jogador_{p}'] = randint(1, 6)

for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogos.items(), key=lambda item: item[1], reverse=True)
print(24*'-=')
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

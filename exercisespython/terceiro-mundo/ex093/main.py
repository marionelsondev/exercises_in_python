jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do Jogador: '))
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, total_partidas):
    partidas.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(30*'-=')
print(jogador)
print(30*'-=')

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')   
print(30*'-=')

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(partidas):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

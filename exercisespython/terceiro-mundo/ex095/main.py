time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    totpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, totpartidas):
        partidas.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        continuar = str(input(f'Quer continuar? [S/N] ').upper()[0])
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if continuar == 'N':
        break

print(30*'-=')
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    qdados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if qdados == 999:
        break
    if qdados >= len(time):
        print(F'ERRO! Não existe jogador com o código {qdados}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[qdados]['nome']}:')

    for i, v in enumerate(time[qdados]['gols']):
        print(f'    No jogo {i+1} fez {v} gols.')
    print(40*'-')
print('<< VOLTE SEMPRE >>')

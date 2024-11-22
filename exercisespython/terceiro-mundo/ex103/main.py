def ficha(nome='<desconhecido>', gol=0):
    return f'O jogador {nome} fez {gol} gol(s) no campeonato.'


nome = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    print(ficha(gol=gol))
else:
    print(ficha(nome, gol))

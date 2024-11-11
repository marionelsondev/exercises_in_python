lista = []
dalunos = []

while True:
    lista.append(str(input(f'Nome: ')))
    lista.append(float(input(f'Nota 1: ')))
    lista.append(float(input(f'Nota 2: ')))
    dalunos.append(lista[:])
    lista.clear()

    continuar = str(input(f'Quer continuar? [S/N] ').upper())

    if continuar[0] != 'S':
        break
    
print(24*'-=')
print(f'No. Nome          MÉDIA')
print(24*'-')

for aluno in enumerate(dalunos):
    print(f'{aluno[0]}   {aluno[1][0]}          {(aluno[1][1] + aluno[1][2]) / 2}')
print(24*'-')

while True:
    qaluno = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))

    if qaluno == 999:
        print('FINALIZANDO...')
        break
    elif qaluno >= 0 and qaluno <= len(dalunos):
        print(f'Notas de {dalunos[qaluno][0]} são [{dalunos[qaluno][1]}, {dalunos[qaluno][2]}]')
    else:
        print('Você digitou um registro inexistente ou um número incorreto! Por favor tente novamente.')

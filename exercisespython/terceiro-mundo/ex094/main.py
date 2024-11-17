pessoas = []
maisvelhos = []
pessoa = {}
totidade = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ').upper()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))

    totidade += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear() 

    while True:
        continuar = str(input('Quer continuar? [S/N] ').split()[0].upper())
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if continuar == 'N':
        break

print(30*'-=')
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = float(totidade / len(pessoas))
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram | ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' | ')

print()
print(f'D) Lista das pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

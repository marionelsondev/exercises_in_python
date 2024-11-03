temp_pessoas = []
lista_pessoas = []
men = mai = 0

while True:
    temp_pessoas.append(str(input('Nome: ')).upper())
    temp_pessoas.append(float(input('Peso: ')))

    if len(lista_pessoas) == 0:
        men = mai = temp_pessoas[1]
    else:
        if temp_pessoas[1] > mai:
            mai = temp_pessoas[1]
        if temp_pessoas[1] < men:
            men = temp_pessoas[1]

    lista_pessoas.append(temp_pessoas[:])
    temp_pessoas.clear()

    continuar = str(input('Quer continuar ? [S/N] ').upper().strip())
    if continuar != 'S':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(lista_pessoas)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='' )
for p in lista_pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='' )
for p in lista_pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

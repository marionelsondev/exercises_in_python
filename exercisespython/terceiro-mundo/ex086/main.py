matriz = []

for i in range(3):
    linha = []
    for e in range(3):
        linha.append(int(input(f'Digite um valor para [{i}, {e}]: ')))
    matriz.append(linha)

print(24*'-=')
for linha in matriz:
    print(linha)

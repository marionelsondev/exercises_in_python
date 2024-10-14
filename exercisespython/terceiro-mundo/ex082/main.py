listanum = []
lista_pares = []
lista_impares = []

while True:
    listanum.append(int(input("Digite um número: ")))
    continuar = str(input("Deseja continuar? [S/N] ").upper())

    if continuar != "S":
        break

for c, v in enumerate(listanum):
    if v % 2 == 0:
        lista_pares.append(v)
    else:
        lista_impares.append(v)
print("-="*24)
print(f"A lista completa é {listanum}")
print(f"A lista de pares é {lista_pares}")
print(f"A lista de ímpares é {lista_impares}")

listanum = []
continuar = ""

while True:
    num = int(input("Digite um valor: "))
    if num not in listanum:
        listanum.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Falha ao adicionar valor! Valor duplicado...")
    continuar = str(input("Quer continuar ? [S/N] ").upper())
    if continuar != "S":
        break
listanum.sort()
print(24*"-=")
print(listanum)

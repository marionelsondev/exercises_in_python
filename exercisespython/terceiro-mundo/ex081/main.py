listanum = []

while True:
    listanum.append(int(input("Digite um valor: ")))
    continuar = str(input("Deseja continuar? [S/N] ").upper())
    if continuar != "S":
        break

print("-="*24)
print(f"Você digitou {len(listanum)} elementos.")

listanum.sort(reverse=True) 
print(f"Os valores em ordem decrescente são {listanum}")

if 5 in listanum:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")

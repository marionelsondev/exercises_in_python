listanum = []

for n in range(0, 5):
    num = int(input("Digite um valor: "))
    if n == 0 or num > listanum[-1]:
        listanum.append(num)
        print("Adicionado ao final da lista...")
    else:
        posicao = 0
        while posicao < len(listanum):
            if num <= listanum[posicao]:
                listanum.insert(posicao, num)
                print(f"Adicionando na posição {posicao} da lista...")
                break
            posicao += 1
print(24*"-=")
print(f"Os valores digitados em ordem foram {listanum}")

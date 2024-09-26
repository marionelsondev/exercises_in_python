lista_numeros = []
lista_numeros_pares = []

for i in range(0, 4):
    lista_numeros.append(int(input("Digite um valor: ")))

valores = tuple(lista_numeros)

print(f"O valor 9 apareceu {valores.count(9)} vezes")
if 3 in valores:
    print(f"O valor 3 apareceu na {valores.index(3) + 1}ª posição")
else:
    print("Não foi digitado em nenhuma posição")
print(f"Os valores pares digitados foram: ", end="")
for num in valores:
    if num % 2 == 0:
        print(f"{num}", end=" ")
print("\n")

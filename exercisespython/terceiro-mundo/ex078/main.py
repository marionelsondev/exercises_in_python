lista_numeros = []

maior = menor = 0

for i in range(0, 5):
    lista_numeros.append(int(input(f"Digite um valor para a Posição {i}: ")))
    if i == 0:
        maior = menor = lista_numeros[i]
    else:
        if lista_numeros[i] > maior:
            maior = lista_numeros[i]
        if lista_numeros[i] < menor:
            menor = lista_numeros[i]

print(f"Você digitou os valores {lista_numeros}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for c, v in enumerate(lista_numeros):
    if v == maior:
        print(f"{c}...", end=" ")
print(f"\nO menor valor digitado foi {menor} nas posições ", end="")
for c, v in enumerate(lista_numeros):
    if v == menor:
        print(f"{c}...", end=" ")

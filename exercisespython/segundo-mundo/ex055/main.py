peso_maior = 0
peso_menor = 0

for p in range(1, 6):
    peso = float(input("Digite um peso: "))
    if p == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f"O maior peso digitado foi: {peso_maior}kg\nO menor peso digitado foi: {peso_menor}kg")

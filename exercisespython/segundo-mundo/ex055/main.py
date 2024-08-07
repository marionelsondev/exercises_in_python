peso_menor = 0
peso_maior = 0

for peso in range(0, 5):
    peso = float(input("Digite um peso: "))
    if peso > peso_maior:
        peso_maior = peso
    else:
        peso_menor = peso
print(f"O maior peso digitado foi: {peso_maior}kg\nO menor peso digitado foi: {peso_menor}kg")

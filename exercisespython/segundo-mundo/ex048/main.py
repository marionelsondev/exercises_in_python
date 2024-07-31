total_soma = 0
total_numero = 0

print("SOMADOR DE NÚMEROS MÚLTIPLOS DE TRÊS QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500")

for numero in range(1, 501, 2):
    if numero%3 == 0:
        total_soma += numero
        total_numero += 1
print(f"A soma de todos os {total_numero} valores solicitados é {total_soma}")

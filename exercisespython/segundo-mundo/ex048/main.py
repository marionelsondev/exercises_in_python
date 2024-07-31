total_soma = 0

print("SOMADOR DE NÚMEROS MÚLTIPLOS DE TRÊS QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500")

for numero in range(1, 501):
    if numero%3 == 0:
        total_soma += numero
print(total_soma)
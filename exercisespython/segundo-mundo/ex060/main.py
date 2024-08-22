num = int(input("Digite um número para calcular o seu fatorial: "))
contador = num
resultado = 1
print (f"Calculando {num}! = ", end="")
while contador > 0:
    print(f"{contador}", end="")
    print(" x " if contador > 1 else " = ", end="")
    resultado *= contador
    contador -= 1
print(f"{resultado}\n", end="")

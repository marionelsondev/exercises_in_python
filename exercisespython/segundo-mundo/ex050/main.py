total_soma = 0
contador = 0

for item in range(1, 7):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        total_soma += num
        contador += 1
print(f"Você informou {contador} números PARES e a soma total é {total_soma}")

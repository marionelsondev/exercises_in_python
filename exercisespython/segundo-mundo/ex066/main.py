cont_num = soma = 0

while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    cont_num += 1
    soma += num
print(f"A soma dos {cont_num} valores foi {soma}!")

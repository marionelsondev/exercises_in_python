cont = total_soma = 0
num = int(input("Digite um número [999 para parar]: "))

while num != 999:
    cont += 1
    total_soma += num
    num = int(input("Digite um número [999 para parar]: "))
print(f"você digitou {cont} números e a soma entre eles foi {total_soma}.")

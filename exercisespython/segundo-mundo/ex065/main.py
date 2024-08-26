continuar = True
maior = menor = total_num = soma = 0

while continuar:
    num = int(input("Digite um número: "))
    total_num += 1
    soma += num
    if total_num == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input("Quer continuar? [S/N] ")).upper()
    if resposta == "N":
        continuar = False
media = soma / total_num
print(f"Você digitou {total_num} números e a média foi {media:.2f}\nO maior valor foi {maior} e o menor foi {menor}")

totnum = 0
totgasto = 0
totmil = 0

print(f"{30*'-'}\n{8*' '}LOJA BULLSEYE{8*' '}\n{30*'-'}")

while True:
    descricao = str(input("Nome do Produto: ")).upper()
    preco = float(input("Preço: R$"))
    totnum += 1
    totgasto += preco
    if preco >= 1000:
        totmil += 1
    if totnum == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = descricao    
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"""O total da compra foi R${totgasto:.2f}
Temos {totmil} produtos custando mais de R$1000.00
O produto mais barato foi {produto_barato} que custa R${menor_preco:.2f}""")

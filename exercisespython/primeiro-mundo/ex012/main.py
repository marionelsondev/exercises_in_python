preco = float(input('Digite o preço do produto em R$:\n'))
desconto = preco*5/100
print(f'-------------------\nValores do produto:\n-------------------\nNormal: R${preco:.2f}\nCom 5% de desconto: R${preco-desconto:.2f}\n')
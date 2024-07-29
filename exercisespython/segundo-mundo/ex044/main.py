print('{:-^40}'.format(' ENKELT STORE '))
preco = float(input("Digite o preço da compra: \033[0;32mR$\033[m"))
cond_pag = int(input('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão\n'''))

if cond_pag == 1:
    desconto = (preco * 10) / 100
    print(f"Sua compra de \033[0;32mR${preco:.2f}\033[m vai custar \033[0;32mR${preco - desconto:.2f}\033[m")
elif cond_pag == 2:
    desconto = (preco * 5) / 100
    print(f"Sua compra de \033[0;32mR${preco:.2f}\033[m vai custar \033[0;32mR${preco - desconto:.2f}\033[m")
elif cond_pag == 3:
    print(f"Sua compra será parcelada em 2x de R${preco / 2:.2f}\nSua compra de \033[0;32mR${preco:.2f}\033[m vai custar \033[0;32mR${preco:.2f}\033[m")
elif cond_pag == 4:
    parcelas = int(input("Quantas parcelas?\n"))
    juros = (preco * 20) / 100
    result_par = (preco + juros) / parcelas
    print(f"Sua compra será parcelada em {parcelas}x de R${result_par:.2f} COM JUROS\nSua compra de \033[0;32mR${preco:.2f}\033[m vai custar \033[0;32mR${preco + juros:.2f}\033[m")
else:
    print("Você digitou uma opção ou um valor inválido. Por favor tente novamente!")

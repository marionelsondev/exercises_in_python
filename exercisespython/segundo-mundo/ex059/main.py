continuar = True
primeiro_valor = float(input("Primeiro valor: "))
segundo_valor = float(input("Segundo valor: "))

while continuar:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
          """)
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        resultado = primeiro_valor + segundo_valor
        print(f"A soma entre {primeiro_valor} + {segundo_valor} é {resultado}")
    elif opcao == 2:
        resultado = primeiro_valor * segundo_valor
        print(f"A multiplicação entre {primeiro_valor} X {segundo_valor} é {resultado}")
    elif opcao == 3:
        if primeiro_valor == segundo_valor:
            print(f"O {primeiro_valor} e o {segundo_valor} são iguais")
        elif primeiro_valor > segundo_valor:
            print(f"{primeiro_valor} é maior que {segundo_valor}")
        else:
            print(f"{segundo_valor} é maior que {primeiro_valor}")
    elif opcao == 4:
        primeiro_valor = float(input("Primeiro valor: "))
        segundo_valor = float(input("Segundo valor: "))
    elif opcao == 5:
        print(f"Programa finalizado!")
        continuar = False
    else:
        print("Você selecionou uma opção inválida e o programa foi finalizado.")
        continuar = False

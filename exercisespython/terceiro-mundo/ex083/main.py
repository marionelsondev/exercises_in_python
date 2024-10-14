expressao = []

lista = str(input("Digite a expressão: "))

paren_aberto = lista.count("(")
paren_fechado = lista.count(")")

if paren_aberto != paren_fechado:
    print("Sua expressão está errada!")
else:
    print("Sua expressão está válida!")

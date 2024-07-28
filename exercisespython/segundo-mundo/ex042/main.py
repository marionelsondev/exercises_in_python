a = float(input("Primeira reta: "))
b = float(input("Segunda reta: "))
c = float(input("Terceira reta: "))

if a < b + c and b < a + c and c < a + b:
    print("As retas acima formam um triângulo ", end="")
    if a == b == c:
        print("EQUILÁTERO!")
    elif a == b or b == c or a == c:
        print("ISÓSCELES!")
    elif a != b and b != c and a != c:
        print("ESCALENO!")
    else:
        print("As retas acima PODEM FORMAR um triângulo mas não se enquadram em nenhum dos tipos de triângulo disponíveis: EQUILÁTERO, ISÓSCELES e ESCALENO.")
else:
    print("\033[0;31mAs retas acima NÃO PODEM formar um triângulo.\033[m")

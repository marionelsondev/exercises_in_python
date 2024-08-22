print(f"{4*" "}[GERADOR DE PA]\n{8*"-=-"}")
termo = int(input("Primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1

while contador <= 10:
    print(f"{termo}", end="")
    print(f" ⭢ " if contador < 10 else " ⭢ FIM\n", end="")
    termo += razao
    contador += 1

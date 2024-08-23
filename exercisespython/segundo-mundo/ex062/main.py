print(f"[GERADOR DE PA V3]")
termo = int(input("Primeiro termo: "))
termo_casa = 10
razao = int(input("Razão da PA: "))
contador = 1

while contador <= termo_casa:
    delimitador = termo_casa
    print(f"{termo}", end="")
    print(f" ⭢ " if contador < delimitador else " ⭢ PAUSA\n", end="")

    if contador == termo_casa:
        termo_casa = termo_casa + int(input("Quantos termos você quer mostrar a mais? "))

    termo += razao
    contador += 1
print(f"Progressão finalizada com {termo_casa} termos mostrados.")

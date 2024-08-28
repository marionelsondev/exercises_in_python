from random import randint

sequencia_vitoria = 0
print(f"{10*'=-='}\n{8*' '}PAR OU ÍMPAR?{8*' '}\n{10*'=-='}")
while True:
    num = int(input("Informe um valor: "))
    num_comp = randint(0, 10)
    total = num + num_comp
    jogada_usuario = ' '

    while jogada_usuario not in "PI":
        jogada_usuario = str(input("Par ou ímpar? [P/I] ")).strip().upper()[0]
    resultado = "PAR" if total % 2 == 0 else "ÍMPAR"
    print(f"{30*'-'}\nVocê jogou {num} e o computador {num_comp}. Total de {total} DEU {resultado}\n{30*'-'}")

    if jogada_usuario == "P" and resultado == "PAR" or jogada_usuario == "I" and resultado == "ÍMPAR":
        print(f"Você VENCEU!\n{10*'=-='}")
        sequencia_vitoria += 1
    else:
        print(f"Você PERDEU!\n{10*'=-='}\nGAME OVER! Você venceu {sequencia_vitoria} vezes.")
        break
    print("Vamos jogar novamente...")

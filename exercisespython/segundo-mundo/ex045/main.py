from random import randint
from time import sleep

jogadas = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''JOGADAS
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
p1 = int(input("Qual é a sua jogada?\n"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print("-"*20)
print(f"CPU jogou {jogadas[cpu]}")
print(f"P1 jogou {jogadas[p1]}")
print("-"*20)
print("RESULTADO: ", end="")

if cpu == 0:
    if p1 == 0:
        print("EMPATE")
    elif p1 == 1:
        print("O P1 VENCEU")
    elif p1 == 2:
        print("A CPU VENCEU")
    else:
        print("JOGADA INVÁLIDA!")
elif cpu == 1:
    if p1 == 0:
        print("A CPU VENCEU")
    elif p1 == 1:
        print("EMPATE")
    elif p1 == 2:
        print("O P1 VENCEU")
    else:
        print("JOGADA INVÁLIDA!")
elif cpu == 2:
    if p1 == 0:
        print("O P1 VENCEU")
    elif p1 == 1:
        print("A CPU VENCEU")
    elif p1 == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!")

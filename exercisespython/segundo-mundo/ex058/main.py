from random import randint
from time import sleep

quant_palpite = 1
num_escolhido = randint(0, 10)

print("[---- ADVINHE O NÚMERO ENTRE 0 E 10 ----]")
num = int(input("Digite o seu palpite: "))
print("PROCESSANDO...")
sleep(1)

while num != num_escolhido:
    num = int(input("Digite um novo palpite: "))
    print("PROCESSANDO...")
    sleep(1)
    quant_palpite += 1
print(f"VOCÊ ACERTOU!\nForam necessários {quant_palpite} palpites para vencer.")

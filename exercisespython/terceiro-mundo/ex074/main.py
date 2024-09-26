from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

print(f"Os valores sorteados foram: ", end="")
for num in numeros:
    print(f"{num}", end=" ")

print(f"\nO maior valor sorteado foi: {max(numeros)}")
print(f"O menor valor sorteado foi: {min(numeros)}")

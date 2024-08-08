idade_maiorm = 0
mulheres = 0
media_idade = 0

for pessoa in range(1, 5):
    print(f"{"-"*5} {pessoa}ª PESSOA {"-"*5}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()

    if sexo == "M" and idade > idade_maiorm:
        idade_maiorm = idade
        nome_maiorm = nome
    if sexo == "F" and idade < 20:
        mulheres += 1
    media_idade += idade
media_idade = media_idade / 4
print(f"A média de idade do grupo é de {media_idade} anos\nO homem mais velho tem {idade_maiorm} anos e se chama {nome_maiorm}.\nAo todo são {mulheres} mulheres com menos de 20 anos")

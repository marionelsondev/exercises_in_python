tot18 = 0
tothomem = 0
totmulher = 0

while True:
    print(f"{30*'-'}\n{5*' '}CADASTRE UM PESSOA{5*' '}\n{30*'-'}")
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

    if idade > 18:
        tot18 += 1
    if sexo == "M":
        tothomem += 1
    if sexo == "F" and idade < 20:
        totmulher += 1

    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print(f"""
Total de pessoas com mais de 18 anos: {tot18}
Ao todo temos {tothomem} homens cadastrados
E temos {totmulher} mulheres com menos de 20 anos""")

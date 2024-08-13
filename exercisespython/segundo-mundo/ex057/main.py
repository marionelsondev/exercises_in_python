continuar = True

sexo = input("Informe seu sexo [M/F]: ").upper()
while continuar:
    if sexo == "M" or sexo == "F":
        print(f"Sexo {sexo} registrado com sucesso.")
        continuar = False
    else:
        sexo = input("Dados inválidos. Por favor, informe seu sexo: ").upper()

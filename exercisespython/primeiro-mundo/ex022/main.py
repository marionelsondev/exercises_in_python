nome = str(input('Qual é o seu nome?\n'))
letras_pnome = nome.split()

print(f'{42*'-'}\nMaiúscula: {nome.upper()}\nMinúscula: {nome.lower()}\nTotal de letras: {len(nome.replace(' ', ''))}\nTotal de letras do primeiro nome({letras_pnome[0]}): {len(letras_pnome[0])}\n{42*'-'}')
nome = str(input('Qual é o seu nome?\n'))
letrasPriNome = nome.split()

print(f'{42*'-'}\nMaiúscula: {nome.upper()}\nMinúscula: {nome.lower()}\nTotal de letras: {len(nome.replace(' ', ''))}\nTotal de letras do primeiro nome({letrasPriNome[0]}): {len(letrasPriNome[0])}\n{42*'-'}')
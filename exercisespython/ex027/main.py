nome = str(input('Digite seu nome completo:\n')).strip().upper()
lista_nome = nome.split()

print(f'Seu primeiro nome é: {lista_nome[0].capitalize()}\nSeu segundo nome é: {lista_nome[len(lista_nome)-1].capitalize()}')

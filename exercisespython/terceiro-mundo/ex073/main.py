tabela = ("Botafogo", "Fortaleza", "Palmeiras", "Flamengo", "Cruzeiro", "São Paulo", "Bahia", "Vasco da Gama", "Atlético Mineiro", "Internacional", "Bragantino", "Athletico-PR", "Criciúma", "Juventude", "Grêmio", "Fluminense", "Corinthians", "Vitória", "Cuiabá", "Atlético Goianiense")
line_length = 30

print(f"{line_length*'-'}\nLista de times do Brasileirão: {tabela}\n{line_length*'-'}")
print(f"Os 5 primeiros são {tabela[0:6]}\n{line_length*'-'}")
print(f"Os 4 últimos são {tabela[-4:]}\n{line_length*'-'}")
print(f"Times em ordem alfabética: {sorted(tabela)}\n{line_length*'-'}")
print(f"O Flamengo está na {tabela.index('Flamengo')+1}º posição\n{line_length*'-'}")

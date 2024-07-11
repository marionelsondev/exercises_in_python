aluguel_dia = int(input('Quantos dias alugados?\n'))
aluguel_km = float(input('Quantos Km rodados?\n'))
diaria = aluguel_dia * 60
kmrodados = aluguel_km * 0.15
print(f'O total a pagar é de R${diaria+kmrodados:.2f}')

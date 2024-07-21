carro_velocidade = float(input('Informe a velocidade do carro em Km/h:\n'))

if carro_velocidade > 80.0:
    print(f'Você foi MULTADO por exceder o limite de 80Km/h.\nMais informações ->>\n|{'-'*54}|\n Velocidade coletada: {carro_velocidade}Km/h\n Valor da multa: R$: {7*(carro_velocidade-80):.2f}\n|{'-'*54}|')
else:
    print(f'Você está dentro do limite de velocidade!\n|{'-'*41}|\n Velocidade coletada: {carro_velocidade}Km/h\n|{'-'*41}|')
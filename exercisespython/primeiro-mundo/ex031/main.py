distancia_viagem = float(input('Digite a distância de uma viagem em KM:\n'))

print(f'{' '*5}[AGÊNCIA DE VIAGENS]{' '*5}')
if distancia_viagem > 200:
    print(f'{'-'*30}\nDistância da viagem: {distancia_viagem}Km\nPreço da passagem: R$: {distancia_viagem * 0.45:.2f}.\n{'-'*30}')
else:
    print(f'{'-'*30}\nDistância da viagem: {distancia_viagem}Km\nPreço da passagem: R$: {distancia_viagem * 0.50:.2f}\n{'-'*30}')
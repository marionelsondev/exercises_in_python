largura_parede = float(input('Digite a largura da parede(m):\n'))
altura_parede = float(input('Digite a altura da parede(m):\n'))
area_parede = largura_parede * altura_parede
quant_tinta = area_parede / 2

print(f'Sua parede tem a dimensão de {largura_parede}x{altura_parede} e sua área é de {area_parede}m². Para pintar essa parede, você precisará de {quant_tinta} litros de tinta.')

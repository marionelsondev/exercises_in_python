import math

angulo_graus = float(input('Digite o ângulo:'))
angulo_radianos = math.radians(angulo_graus)

print(f'sin({angulo_graus}): {math.sin(angulo_radianos):.2f}\ncos({angulo_graus}): {math.cos(angulo_radianos):.2f}\ntan({angulo_graus}): {math.tan(angulo_radianos):.2f}')
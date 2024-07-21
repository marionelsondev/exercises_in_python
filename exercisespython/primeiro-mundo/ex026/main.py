frase = str(input('Digite uma frase:\n')).strip().upper()

print(f'Total de letras "A": {frase.count('A')}')
print(f'Posição do primeiro "A": {frase.find('A')+1}')
print(f'Posição do último "A": {frase.rfind('A')+1}')
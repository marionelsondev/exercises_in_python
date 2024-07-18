ano = int(input('Informe um ano(ex. 2024) para saber se ele é bissexto ou não:\n'))

if ano % 4 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto.')
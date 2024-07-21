num = int(input('Digite um número para descobrir se ele é par ou ímpar:\n'))
verificar_paridade = num % 2

if verificar_paridade == 0:
    print(f'|{'-'*17}|\n O número {num} é PAR.\n|{'-'*17}|')
else:
    print(f'|{'-'*20}|\n O número {num} é ÍMPAR.\n|{'-'*20}|')
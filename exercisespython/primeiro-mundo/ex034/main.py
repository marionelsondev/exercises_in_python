salario = float(input('Digite o salário: R$:'))

if salario > 1250:
    print(f'Você obteve um aumento de 10%:\nR$:{salario+(salario*10/100):.2f}')
else:
    print(f'Você obteve um aumento de 15%:\nR$:{salario+(salario*15/100):.2f}')
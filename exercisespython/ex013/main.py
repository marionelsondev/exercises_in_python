salario_func = float(input('Digite o seu salário em R$:\n'))
aumento = (15/100)*salario_func
print(f'Você ganhou um aumento de 15% no seu salário!!!\nSalário antigo: R${salario_func:.2f}\nNovo salário (com aumento de 15%): R$ {salario_func+aumento:.2f}')
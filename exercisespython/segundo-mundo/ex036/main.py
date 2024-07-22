from time import sleep

print(f'{' '*20}\033[0;36m[BANCO]\033[m{' '*20}\n{'-'*50}')
print('Olá, eu sou o \033[0;35mMorgan\033[m!')
sleep(2) 
print('Irei lhe acompanhar durante o processo do empréstimo bancário!')

preco_casa = float(input('Digite o preço da casa que deseja comprar: R\033[0;32m$\033[m'))
salario_comprador = float(input('Digite o salário do comprador: '))
anos_financiamento = int(input('Em quantos anos o comprador pretende pagar?\n'))

pagamento_meses = anos_financiamento * 12
prestacao = preco_casa / pagamento_meses

if prestacao <= salario_comprador*30/100:
    print('\033[0;32mEmpréstimo APROVADO!\033[m')
    print(f'\033[0;32mPara pagar uma casa de {preco_casa:.2f} a pretação será de R$: {prestacao:.2f} em {pagamento_meses}x\033[m')
else:
    print('\033[0;31mEmpréstimo NEGADO.\033[m')
    print('\033[0;31mO empréstimo que você deseja fazer excede o limite de 30% baseado no seu salário atual.\033[m')
    print(f'\033[0;31mPara pagar uma casa de {preco_casa:.2f} a prestação será de R$: {prestacao:.2f} em {pagamento_meses}x\033[m')
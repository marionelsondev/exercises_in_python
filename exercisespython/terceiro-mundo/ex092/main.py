from datetime import date

ano_atual = date.today().year

colaborador = {}

colaborador['nome'] = str(input('Nome: '))
colaborador['idade'] = ano_atual - int(input('Ano de nascimento: '))
colaborador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if colaborador['ctps'] != 0:
    colaborador['ano_contratacao'] = int(input('Ano de Contratação: '))
    colaborador['salario'] = float(input('Salário: R$'))
    colaborador['aposentadoria'] = colaborador['idade'] + (colaborador['ano_contratacao'] + 35) - ano_atual

print(24*'-=')
for k, v in colaborador.items():
    print(f'  - {k} tem o valor de {v}')

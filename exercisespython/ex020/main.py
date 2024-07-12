from random import shuffle

alunos = []

for i in range(4):
    alunos.append(str(input('Digite o nome do aluno(a):')))

shuffle(alunos)
print(f'A ordem de apresentação será\n{alunos}')

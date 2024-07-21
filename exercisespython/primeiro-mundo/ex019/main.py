import random

alunos = []

for i in range(4):
    alunos.append(str(input('Digite o nome do aluno(a) que deseja cadastrar:')))

print(f'{alunos[random.randint(0, 3)]} irá apagar o quadro.\n')
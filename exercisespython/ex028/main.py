import random

num_comp = random.randint(0, 5)
num_user = int(input('Adivinhe o número entre 0 a 5:\n'))

if num_user == num_comp:
    print('Parabéns, você adivinhou o número!')
else:
    print('Não foi dessa vez :(')
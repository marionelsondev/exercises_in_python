from random import randint
from time import sleep

num_comp = randint(0, 5)
print('-'*54)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-'*54)
num_usuario = int(input('Em que número eu pensei?\n'))
print('PROCESSANDO...')
sleep(2)

if num_usuario== num_comp:
    print('Parabéns! Você venceu!')
else:
    print(f'Você perdeu. O número pensado foi {num_comp}, você digitou {num_usuario}.')
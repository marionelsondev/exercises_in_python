from pygame import mixer
from time import sleep

print(f"CONTAGEM REGRESSIVA PARA O ESTOURO DOS FOGOS DE ARTIFÍCIOS\n{"-"*58}")
mixer.init()
mixer.music.load(r"C:\Users\Mario\Documents\projects\cursoemvideo_exercises\exercisespython\segundo-mundo\ex046\assets\fireworks.mp3")
for contador in range(10, 0, -1):
    print(contador)
    sleep(1)
mixer.music.play()
stop = input("Pressione qualquer tecla para encerrar o áudio...\n")

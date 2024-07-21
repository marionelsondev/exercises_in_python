from pygame import mixer

mixer.init()
mixer.music.load(r'C:\Users\MARIO.NETO\Documents\cursoemvideo_exercises\exercisespython\ex021\assets\michaelia.mp3')
mixer.music.play()
stop = input('Digite algo para parar a música...\n')
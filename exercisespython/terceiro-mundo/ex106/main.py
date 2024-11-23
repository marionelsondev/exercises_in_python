from time import sleep

colors = ('\033[m', '\033[1;30;41m', '\033[1;30;44m', '\033[1;30;47m')

def ajuda(prompt):
    print(customtitle(f'Acessando o manual do comando "{prompt}"', 2))
    help(prompt)
    sleep(1)

    return ''

def customtitle(msg, colorchoice=0):
    tam = len(msg) + 4
    print(tam * f'{colors[colorchoice]}~\033[m')
    print(f'{colors[colorchoice]}  {msg}  \033[m')
    print(tam * f'{colors[colorchoice]}~\033[m')
    sleep(1)

    return ''

cmd = ''

while True:
    print(customtitle('SISTEMA DE AJUDA PyHELP', 1))
    cmd = str(input('Função ou Biblioteca > '))
    if cmd.upper().strip() == 'FIM':
        break
    else:
        print(ajuda(cmd))
print(customtitle('ATÉ LOGO!', 1))

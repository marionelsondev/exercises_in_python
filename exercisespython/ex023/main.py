num_incorreto = True
casa = ['Unidade', 'Dezena', 'Centena', 'Milhar']
while num_incorreto:
    num = int(input('Digite um número entre 0 e 9999:\n'))
    num_string = str(num)
    if num > 0 and num < 9999:
        for elemento in range(len(num_string)):
            print(f'{casa[elemento]} {num_string[elemento]}') 
        num_incorreto = False
    else:
        print('Você digitou um número incorreto, por favor tente novamente!')
        num_incorreto = True

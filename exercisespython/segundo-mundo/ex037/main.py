num = int(input('Digite um número inteiro:'))
option = int(input('Para qual base deseja converter?\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL\n'))
num_conv = []

def inverter_lista_slicing(lista):
    return lista[::-1]

if option == 1:
    while num / 2 != 0:
        resto = num % 2
        num = num // 2
        num_conv.append(resto)
        inverter_lista_slicing(num_conv)
    print(num_conv)
elif option == 2:
    print()
else:
    print()

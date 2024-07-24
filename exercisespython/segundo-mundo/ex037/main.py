import utils

num = int(input("Digite um número inteiro:"))
option = int(input("Para qual base deseja converter?\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL\n"))
num_conv = 0

if option == 1:
    num_conv = utils.inteiro_binario(num)
    print(f"O número {num} convertido para binário é: {num_conv}")
elif option == 2:
    num_conv = utils.inteiro_octal(num)
    print(f"O número {num} convertido para octal é: {num_conv}")
elif option == 3:
    num_conv = utils.inteiro_hexadecimal(num)
    print(f"O número {num} convertido para hexadecimal é: {num_conv}")
else:
    print("Opção inválida, por favor tente novamente.")

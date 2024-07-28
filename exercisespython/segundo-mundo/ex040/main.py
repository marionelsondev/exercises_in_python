from time import sleep

print("BEM-VINDO AO SISTEMA DE GESTÃO DE NOTAS ESCOLARES")
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2)/2

if media < 5 and media >= 0:
    print("Processando...")
    sleep(1)
    print(f"\033[0;31mMÉDIA DO ALUNO: {media:.2f}\nSITUAÇÃO: REPROVADO\033[m")
elif media >= 5 and media < 7:
    print("Processando...")
    sleep(1)
    print(f"\033[0;33mMÉDIA DO ALUNO: {media:.2f}\nSITUAÇÃO: RECUPERAÇÃO\033[m")
elif media >= 7 and media <= 10:
    print("Processando...")
    sleep(1)
    print(f"\033[0;32mMÉDIA DO ALUNO: {media:.2f}\nSITUAÇÃO: APROVADO\033[m")
else:
    print("\033[0;31mOcorreu um erro ao tentar calcular a média.\033[m")

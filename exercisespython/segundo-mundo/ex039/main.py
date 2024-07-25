from datetime import date

ano_nasc = int(input("Digite o seu ano de nascimento:\n"))
sexo = int(input("Informe o seu sexo:\n[1] MASCULINO\n[2] FEMININO\n"))
idade = date.today().year - ano_nasc
tempo_res = 18 - idade
tempo_exc = idade - 18

if sexo == 1:
    if idade < 18 and idade > 0:
        print(f"AINDA não chegou o momento do seu alistamento, confira abaixo o tempo restante para o seu     alistamento:\n\033[0;36mTEMPO RESTANTE: {18 - idade} ano(s)\nANO DE NASCIMENTO: {ano_nasc}\nIDADE     ATUAL: {idade}\nANO DO ALISTAMENTO: {date.today().year + tempo_res}\033[m")
    elif idade > 18 and idade < 130:
        print(f"JÁ passou da hora do seu alistamento, procure a junta de serviço militar mais próxima,     confira abaixo o tempo excedido do prazo:\n\033[0;31mTEMPO EXCEDIDO: {idade - 18} ano(s)\nANO DE     NASCIMENTO: {ano_nasc}\nIDADE ATUAL: {idade}\033[m")
    elif idade == 18:
        print(f"Você está no momento \033[0;32mEXATO\033[m para realizar o seu alistamento, procure a     junta de serviço militar mais próxima!\n\033[0;32mANO DE NASCIMENTO: {ano_nasc}\nIDADE ATUAL:     {idade}\nANO DO ALISTAMENTO: {date.today().year}\033[m")
    else:
        print("Você digitou uma idade inválida, por favor tente novamente!")
elif sexo == 2:
    print("Você não é obrigada a se alistar no exército.")
else:
    print("Você digitou uma opção inválida!")
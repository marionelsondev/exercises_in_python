from datetime import date

ano_nasc = int(input("Digite o seu ano de nascimento:\n"))
idade = date.today().year - ano_nasc

if idade < 18 and idade > 0:
    print(f"AINDA não chegou o momento do seu alistamento, consulte a abaixo o tempo restante para o seu alistamento:\n\033[0;36mTEMPO RESTANTE: {18 - idade} ano(s)\033[m")
elif idade > 18 and idade < 130:
    print(f"JÁ passou da hora do seu alistamento, procure a junta de serviço militar mais próxima, confira abaixo o tempo excedido do prazo:\n\033[0;31mTEMPO EXCEDIDO: {idade - 18} ano(s)\033[m")
elif idade == 18:
    print(f"Você está no \033[0;32mMOMENTO EXATO\033[m para realizar o seu alistament, procure a junta de serviço militar mais próxima!")
else:
    print("Você digitou uma idade inválida, por favor tente novamente!")

from datetime import date

print(f"\033[1;36mSISTEMA DE CATEGORIAS DA CONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m\n{57*"-"}")
ano_atual = date.today().year
ano_nasc = int(input("Digite o ano de nascimento do atleta: "))
idade_atleta = ano_atual - ano_nasc

if idade_atleta <= 9 and idade_atleta >= 1:
    print(f"{15*"-=-"}\n            INFORMAÇÕES DO ATLETA\n{15*"-=-"}\nIDADE: {idade_atleta}\nCATEGORIA: \033[1;37mMIRIM\033[m")
elif idade_atleta <= 14:
    print(f"{15*"-=-"}\n            INFORMAÇÕES DO ATLETA\n{15*"-=-"}\nIDADE: {idade_atleta}\nCATEGORIA: \033[1;32mINFANTIL\033[m")
elif idade_atleta <= 19:
    print(f"{15*"-=-"}\n            INFORMAÇÕES DO ATLETA\n{15*"-=-"}\nIDADE: {idade_atleta}\nCATEGORIA: \033[1;34mJÚNIOR\033[m")
elif idade_atleta <= 25:
    print(f"{15*"-=-"}\n            INFORMAÇÕES DO ATLETA\n{15*"-=-"}\nIDADE: {idade_atleta}\nCATEGORIA: \033[1;35mSÊNIOR\033[m")
elif idade_atleta > 25 and idade_atleta <= 130:
    print(f"{15*"-=-"}\n            INFORMAÇÕES DO ATLETA\n{15*"-=-"}\nIDADE: {idade_atleta}\nCATEGORIA: \033[1;33mMASTER\033[m")
else:
    print("\033[0;31mOcorreu um erro ao identificar a sua categoria, verifique se o ano de nascimento está correto!\033[m")

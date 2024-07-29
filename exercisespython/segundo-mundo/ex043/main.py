peso = float(input("Digite o seu peso (Kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = peso / (altura**2)

print(f"{10*"-=-"}\n         INFORMAÇÕES\n{10*"-=-"}\nPESO: {peso:.1f}kg\nALTURA: {altura}cm\nIMC: {imc:.1f}kg/m2\nCATEGORIA: ", end="")
if imc > 0 and imc < 18.5:
    print("\033[0;31mABAIXO DO PESO\033[m")
elif imc >= 18.5 and imc < 25:
    print("\033[0;32mPESO IDEAL\033[m")
elif imc >= 25 and imc < 30:
    print("\033[0;33mSOBREPESO\033[m")
elif imc >= 30 and imc < 40:
    print("\033[0;31mOBESIDADE\033[m")
elif imc >= 40:
    print("\033[0;31mOBESIDADE MÓRBIDA\033[m")
else:
    print("\033[0;31mNão foi possível categorizar o seu IMC, verifique se inseriu os dados corretamente.\033[ms")

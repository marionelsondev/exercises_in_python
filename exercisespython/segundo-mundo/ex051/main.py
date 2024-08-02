termo = int(input("Digite o termo inicial: "))
razao = int(input("Digite a razão: "))
enesimo = 1
resultados = []

for contador in range(10):
    resultado = termo + (enesimo - 1) * razao
    resultados.append(resultado)
    enesimo += 1
resul_conv = str(resultados)
print(f"Aqui estão os \033[1;35m10\033[m primeiros termos da progressão (TERMO: {termo} RAZÃO: {razao})\n{resul_conv.strip('[]')}")

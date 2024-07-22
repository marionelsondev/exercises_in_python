retaa = float(input('Digite o comprimento da reta A: '))
retab = float(input('Digite o comprimento da reta B: '))
retac = float(input('Digite o comprimento da reta C: '))

if retaa + retab > retac and retaa + retac > retab and retab + retac > retaa:
    print(f'As retas com os seguintes comprimentos podem formar um triângulo:\nReta A: {retaa}\nReta B: {retab}\nReta C: {retac}')
else:
    print(f'As retas com os seguintes comprimentos \033[1;31mNÃO\033[m podem formar um triângulo:\nReta A: {retaa}\nReta B: {retab}\nReta C: {retac}')